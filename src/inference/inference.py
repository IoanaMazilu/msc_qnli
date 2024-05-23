# !pip install -q accelerate==0.21.0 peft==0.4.0 bitsandbytes==0.40.2 transformers==4.31.0 trl==0.4.7
import argparse
from dotenv import load_dotenv
import gc
import logging
import os
import numpy as np
import pandas as pd
import time
import traceback

from datasets import Dataset
from peft import PeftModel
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    pipeline,
    logging,
)
from transformers.pipelines.pt_utils import KeyDataset

from config import *

load_dotenv()


def add_lora_adapters_to_model(base_model, input_path, model_name, model_size):
    """Reload model in FP16 and merge it with LoRA weights"""
    target_model_path = os.path.join(input_path, "input", "model", f"{model_name}-{model_size}")
    try:
        ft_model = PeftModel.from_pretrained(base_model, target_model_path)
    except Exception:
        print("###### FAILED TO LOAD PEFT MODEL ######")
        print(traceback.print_exc())
        return None, None
    return ft_model.merge_and_unload()


def load_tokenizer(hf_repo: str, cache_directory: str, finetuned: bool):
    """Loads a tokenizer from a pretrained one and updates the padding token if the tokenizer will be used with a
    fine-tuned model. Also, set the padding side to right (specific to Llama models)."""
    # Load LLaMA tokenizer
    print("Loading the tokenizer...")
    start_time = time.time()
    tokenizer = AutoTokenizer.from_pretrained(
        hf_repo,
        token=os.getenv("HF_TOKEN"),
        trust_remote_code=True,
        cache_dir=cache_directory)
    print(f"###### EOS token: {tokenizer.eos_token} ######")
    if tokenizer.eos_token is None:
        tokenizer.eos_token = "</s>"
    print(f"###### PAD token: {tokenizer.pad_token} ######")
    if tokenizer.pad_token is None and finetuned:
        print("##### Setting PAD token to <pad> for fine-tuned models ######")
        tokenizer.add_special_tokens({"pad_token": "<pad>"})
    print(f"TOKENIZER PADDING SIDE: {tokenizer.padding_side}")
    tokenizer.padding_side = "right"  # Fix weird overflow issue with fp16 training
    print(f"Tokenizer loaded in {round((time.time() - start_time) / 60, 2)} min.")
    return tokenizer


def load_model(hf_repo: str, finetuned: bool, input_path: str, model_name: str, model_size: str):

    # download models on scratch disk
    cache_directory = os.path.join(input_path, "cached_pretrained_model")

    # Load tokenizer and model (use 4bits loading configuration)
    compute_dtype = getattr(torch, bnb_4bit_compute_dtype)
    print(f"Compute type: {compute_dtype}")

    # Load LLaMA tokenizer
    tokenizer = load_tokenizer(hf_repo, cache_directory, finetuned)

    # Load base model
    print("Loading the model...")
    start_time = time.time()

    if not finetuned:
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=use_4bit,
            bnb_4bit_quant_type=bnb_4bit_quant_type,
            bnb_4bit_compute_dtype=compute_dtype,
            bnb_4bit_use_double_quant=use_nested_quant,
        )

        model = AutoModelForCausalLM.from_pretrained(
            hf_repo,  # use default value if none provided
            # quantization_config=bnb_config,
            torch_dtype=torch.float16,
            device_map=device_map,
            token=os.getenv("HF_TOKEN"),
            cache_dir=cache_directory
        )
        # model.config.use_cache = False
        # model.config.pretraining_tp = 1
    else:
        base_model = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=hf_repo,
            token=os.getenv("HF_TOKEN"),
            low_cpu_mem_usage=True,
            return_dict=True,
            torch_dtype=torch.float16,
            device_map=device_map,
            cache_dir=cache_directory
        )
        base_model.resize_token_embeddings(len(tokenizer))
        # tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids("<pad>")
        base_model.config.pad_token_id = tokenizer.pad_token_id
        model = add_lora_adapters_to_model(base_model, input_path, model_name, model_size)
    print(f"Model loaded in {round((time.time() - start_time) / 60, 2)} min.")

    return model, tokenizer


def format_prompt_for_inference(prompt: str, prompt_template: str, finetuned_model: bool = False) -> str:
    # if not finetuned_model:
    sys_msg = "Give a response suitable to the instructions below"
    if prompt_template == "llama2":
        prompt = f"<s>[INST]\n<<SYS>>\n{sys_msg}\n<</SYS>>\n\n{prompt}[/INST]"
    elif prompt_template == "inputs_only":
        # inputs = prompt.split("### Input:")[1].lstrip("\n")
        # prompt = f"<s>[INST]{inputs}[/INST]"
        instruction = prompt.split(" To illustrate, ")[0]
        input_part = prompt.rsplit("END_EXAMPLE", maxsplit=1)[1]
        new_prompt = f"{instruction}{input_part}"
        text = f"<s>[INST]\n<<SYS>>\n{sys_msg}\n<</SYS>>\n\n{new_prompt}[/INST]"

    if finetuned_model:
        prompt += "\n### Response:\n"

    return prompt


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='QNLI prediction')
    parser.add_argument('-j', '--job-id', required=True,
                        help="Unique identifier for this experiment, set this to the ID of the slurm job.")
    parser.add_argument('--model-name', default="llama-2", required=True,
                        help="The name of the model (i.e. llama-2, code-llama, mistral.")
    parser.add_argument('--model-size', default="7B", required=True,
                        help="The size of the model.")
    parser.add_argument('--hf-repo', default="meta-llama/Llama-2-7b-hf",
                        required=False, help="The name of the HF repo for the model.")
    parser.add_argument('--max-new-tokens', default="512",
                        required=False, help="Max tokens to generate for the completion.")
    parser.add_argument('--batch-size', default="8",
                        required=False, help="Batch size to use for generation pipeline")
    parser.add_argument('--finetuned', required=False, action="store_true")
    parser.add_argument('--sample-size', required=False, default=None)
    parser.add_argument('--split-set', required=False, action="store_true")
    parser.add_argument("-i", "--input-path", help="The path to the datasets", required=True)
    parser.add_argument("-o", "--output-path", help="The output path to save the fine-tuned model data", required=True)
    parser.add_argument("--prompt-template", required=False, default="llama-2",
                        choices=["llama2", "llama3", "inputs_only"])

    args = parser.parse_args()

    print(f"FINETUNED MODEL: {args.finetuned}")
    if args.finetuned:
        print(f"Fine-tuned model ID: {args.job_id}")
    else:
        print(f"JOB ID: {args.job_id}")
    print(f"MODEL NAME: {args.model_name}")
    print(f"MODEL SIZE: {args.model_size}")
    print(f"HF REPO: {args.hf_repo}")
    print(f"MAX-NEW-TOKENS {args.max_new_tokens}")
    print(f"BATCH SIZE {args.batch_size}")
    print(f"SPLIT SET IN BATCHES {args.split_set}")
    print(f"PROMPT TEMPLATE: {args.prompt_template}")

    logging.get_logger("transformers").setLevel(logging.ERROR)  # Suppresses info and warning messages from transformers

    print("########## LOADING THE DATA ##########")
    if args.sample_size is None:
        nrows = None
    else:
        nrows = int(args.sample_size)
    test_dataset = pd.read_csv(os.path.join(args.input_path, "input", "completion", f'test_all.csv'), nrows=nrows)
    print(f"Loaded {test_dataset.shape[0]} test samples.")
    print(f"Dataset features: {test_dataset.columns}")

    print("########## PREPARING THE DATA FOR INFERENCE ##########")
    test_dataset["input_prompt"] = test_dataset["prompt"].apply(lambda prompt: format_prompt_for_inference(prompt, args.prompt_template, args.finetuned))

    batch_count = 4 if args.split_set else 1
    splits_as_df = []
    splits = []
    batch_size = test_dataset.shape[0] // batch_count
    for i in range(batch_count):
        split = test_dataset.iloc[i*batch_size:(i+1)*batch_size]
        split_as_dict = split.to_dict(orient="list")
        splits.append(KeyDataset(Dataset.from_dict(split_as_dict), "input_prompt"))
        splits_as_df.append(split)

    # # we need a datasets.Dataset object for GPU-optimized inference with a pipeline
    # dataset_as_dict = test_dataset.to_dict(orient="list")
    # iterable_dataset = KeyDataset(Dataset.from_dict(dataset_as_dict), "input_prompt")

    print("########## LOADING THE MODEL AND TOKENIZER ##########")
    model, tokenizer = load_model(args.hf_repo, args.finetuned, args.input_path, args.model_name, args.model_size)
    model.bfloat16()
    if model.config.pad_token_id is None and not args.finetuned:
        model.config.pad_token_id = model.config.eos_token_id
    pipe = pipeline(task="text-generation",
                    model=model,
                    tokenizer=tokenizer,
                    max_new_tokens=int(args.max_new_tokens),
                    return_full_text=False)
    # if "code" in args.hf_repo and not args.finetuned:
    #     # CodeLlama asks for this configuration (unless it is our fine-tuned model)
    if not args.finetuned:
        pipe.tokenizer.pad_token_id = model.config.eos_token_id
    try:
        print("#################### GENERATING COMPLETIONS FOR THE TEST SET  ####################")
        start_time = time.time()
        idx = 0
        for split_as_df, iterable_split in zip(splits_as_df, splits):
            idx += 1
            completions = []
            for completion in pipe(iterable_split, batch_size=int(args.batch_size)):
                try:
                    extracted_completion = completion[0]['generated_text']
                except:
                    extracted_completion = np.nan
                completions.append(extracted_completion)
            split_as_df["inferred_script"] = completions
            split_as_df.to_csv(os.path.join(args.output_path, "output", f"test_{idx}.csv"), index=False)
        print(f"GPU-efficient inference: {round(time.time() - start_time, 2)} seconds.")
    except:
        print("Error during inference.")
        print(traceback.print_exc())
    finally:
        # Empty VRAM
        del model
        del tokenizer
        del pipe
        gc.collect()
        gc.collect()
