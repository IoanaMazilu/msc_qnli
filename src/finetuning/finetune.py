# !pip install -q accelerate==0.21.0 peft==0.4.0 bitsandbytes==0.40.2 transformers==4.31.0 trl==0.4.7
import argparse
from dotenv import load_dotenv
import os
import pandas as pd
import time
import traceback

import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    pipeline,
    logging,
)
from peft import LoraConfig, PeftModel
from trl import SFTTrainer, DataCollatorForCompletionOnlyLM
from training_configuration import *

load_dotenv()


# torch.cuda.empty_cache()


def load_data(split: str, input_path: str = None):
    data_directory_path = input_path if input_path else os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "data")
    cache_directory = os.path.join(input_path, "cached_data")
    return load_dataset('csv',
                        data_files=os.path.join(data_directory_path,
                                                "input",
                                                "completion",
                                                f'{split}_all.csv'),
                        split="train",
                        cache_dir=cache_directory)


def prepare_model_for_fine_tuning(custom_output_dir: str,
                                  learning_rate: float,
                                  warmup_ratio: float,
                                  epochs: int,
                                  padding_token: str,
                                  input_path: str,
                                  train_dataset=None,
                                  eval_dataset=None,
                                  custom_model_name: str = None):
    # download models on scratch
    cache_directory = os.path.join(input_path, "cached_pretrained_model")

    # Load tokenizer and model with QLoRA configuration
    compute_dtype = getattr(torch, bnb_4bit_compute_dtype)
    print(f"Compute type: {compute_dtype}")

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=use_4bit,
        bnb_4bit_quant_type=bnb_4bit_quant_type,
        bnb_4bit_compute_dtype=compute_dtype,
        bnb_4bit_use_double_quant=use_nested_quant,
    )

    # Check GPU compatibility with bfloat16
    if compute_dtype == torch.float16 and use_4bit:
        print("Check if GPU compatible with bfloat16")
        major, _ = torch.cuda.get_device_capability()
        if major >= 8:
            print("=" * 10)
            print("Your GPU supports bfloat16: accelerate training with bf16=True")
            print("=" * 10)

    # Load base model
    print("Loading the model...")
    start_time = time.time()
    model = AutoModelForCausalLM.from_pretrained(
        custom_model_name if custom_model_name else model_name,  # use default value if none provided
        quantization_config=bnb_config,
        device_map=device_map,
        cache_dir=cache_directory
    )
    model.config.use_cache = False
    model.config.pretraining_tp = 1
    print(f"Model loaded in {round((time.time() - start_time) / 60, 2)} min.")

    # Load LLaMA tokenizer
    print("Loading the tokenizer...")
    start_time = time.time()
    tokenizer = AutoTokenizer.from_pretrained(
        custom_model_name if custom_model_name else model_name,
        use_auth_token=True,
        # token=os.getenv("HF_TOKEN"),
        trust_remote_code=True,
        cache_dir=cache_directory)

    print(f"###### EOS token: {tokenizer.eos_token} ######")
    if tokenizer.eos_token is None:
        tokenizer.eos_token = "</s>"
    print(f"###### PAD token: {tokenizer.pad_token} ######")
    if tokenizer.pad_token is None:
        if padding_token == "eos":
            print("##### Setting PAD token to EOS token ######")
            tokenizer.pad_token = tokenizer.eos_token
        else:
            print("##### Setting PAD token to <pad> token ######")
            tokenizer.add_special_tokens({"pad_token": "<pad>"})
            model.resize_token_embeddings(len(tokenizer))
            # tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids("<pad>")
            model.config.pad_token_id = tokenizer.pad_token_id
    tokenizer.padding_side = "right"  # Fix weird overflow issue with fp16 training
    print(f"Tokenizer loaded in {round((time.time() - start_time) / 60, 2)} min.")

    # Load LoRA configuration
    peft_config = LoraConfig(
        lora_alpha=lora_alpha,
        lora_dropout=lora_dropout,
        r=lora_r,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=['v_proj', 'down_proj', 'up_proj', 'q_proj', 'gate_proj', 'k_proj', 'o_proj']
    )

    # Set training parameters
    training_arguments = TrainingArguments(
        output_dir=custom_output_dir,
        evaluation_strategy="steps" if eval_dataset else "no",
        save_strategy="epoch",
        num_train_epochs=epochs,
        per_device_train_batch_size=per_device_train_batch_size,
        # per_device_eval_batch_size=per_device_eval_batch_size,
        gradient_accumulation_steps=gradient_accumulation_steps,
        gradient_checkpointing=gradient_checkpointing,
        optim=optim,
        save_steps=save_steps,
        logging_steps=logging_steps,
        learning_rate=learning_rate,
        weight_decay=weight_decay,
        fp16=fp16,
        bf16=bf16,
        max_grad_norm=max_grad_norm,
        max_steps=max_steps,
        warmup_ratio=warmup_ratio,
        group_by_length=group_by_length,
        lr_scheduler_type=lr_scheduler_type,
        report_to=["tensorboard"],
    )

    def formatting_prompts_func(example):
        output_texts = []
        for i in range(len(example['prompt'])):
            # pre_instruction = "Below is an instruction that describes a task. Write a response that appropriately completes the request."
            # text = f"{pre_instruction}\n\n{example['prompt'][i]}\n\n### Response:\n{example['completion'][i]}</s>"
            sys_msg = "Give a response suitable to the instructions below"
            text = f"<s>[INST]\n<<SYS>>\n{sys_msg}\n<</SYS>>\n\n{example['prompt'][i]}[/INST]\n### Response:\n{example['completion'][i]}</s>"
            output_texts.append(text)
        return output_texts

    # https://huggingface.co/docs/trl/main/en/sft_trainer#using-tokenids-directly-for-responsetemplate
    # add some context to the response_template, to get the correct tokens matching those in the formatted prompt
    response_template_with_context = "add some context\n### Response:\n"
    response_template_ids = tokenizer.encode(response_template_with_context, add_special_tokens=False)
    collator = DataCollatorForCompletionOnlyLM(response_template_ids[4:], tokenizer=tokenizer, mlm=False)

    # Set supervised fine-tuning parameters
    trainer = SFTTrainer(
        model=model,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        peft_config=peft_config,
        # dataset_text_field="text",
        max_seq_length=max_seq_length,
        tokenizer=tokenizer,
        args=training_arguments,
        packing=packing,
        data_collator=collator,
        formatting_func=formatting_prompts_func,
        dataset_batch_size=8
    )
    return model, tokenizer, trainer


# Train model
def train(model, trainer, target_model_path):
    trainer.train()

    # Save trained model
    print("Saving fine-tuned model...")
    trainer.model.save_pretrained(target_model_path)

    # Empty VRAM
    del model
    del trainer
    import gc
    gc.collect()
    gc.collect()


def load_fine_tuned_model(target_model_path: str,
                          padding_token: str,
                          source_model_name: str,
                          input_path: str):

    # download models on scratch
    cache_directory = os.path.join(input_path, "cached_pretrained_model")

    # Reload tokenizer to save it
    tokenizer = AutoTokenizer.from_pretrained(source_model_name, trust_remote_code=True, cache_dir=cache_directory)
    if tokenizer.pad_token is None:
        if padding_token == "eos":
            print("##### Setting PAD token to EOS token ######")
            tokenizer.pad_token = tokenizer.eos_token
        else:
            print("##### Setting PAD token to <pad> token ######")
            tokenizer.add_special_tokens({"pad_token": "<pad>"})
            # tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids("<pad>")
    tokenizer.padding_side = "right"

    # Reload model in FP16 and merge it with LoRA weights
    base_model = AutoModelForCausalLM.from_pretrained(
        source_model_name if source_model_name else model_name,
        low_cpu_mem_usage=True,
        return_dict=True,
        torch_dtype=torch.float16,
        device_map=device_map,
        cache_dir=cache_directory
    )
    base_model.resize_token_embeddings(len(tokenizer))
    base_model.config.pad_token_id = tokenizer.pad_token_id
    try:
        ft_model = PeftModel.from_pretrained(base_model, target_model_path)
        print("PEFT Model needs path to saved fine-tuned model")
    except Exception:
        print("###### FAILED TO LOAD PEFT MODEL ######")
        print(traceback.print_exc())
        return None, None
    ft_model = ft_model.merge_and_unload()

    return ft_model, tokenizer


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='QNLI prediction')

    parser.add_argument('-j', '--job-id', required=True,
                        help="Unique identifier for this experiment, set this to the ID of the slurm job.")
    parser.add_argument('--model-name', default="llama-2", required=True,
                        help="The name of the model (i.e. llama-2, code-llama, mistral.")
    parser.add_argument('--model-size', default="7B", required=True,
                        help="The size of the model.")
    parser.add_argument('--hf-repo', default="meta-llama/Llama-2-7b-hf",
                        required=True, help="The name of the HF repo for the model.")
    parser.add_argument('--learning-rate', required=True)
    parser.add_argument('--warmup-ratio', required=True)
    parser.add_argument('--pad-token', required=True, choices=["eos", "pad"])
    parser.add_argument('--epochs', required=True)
    parser.add_argument("-i", "--input-path", help="The path to the datasets", required=True)
    parser.add_argument("-o", "--output-path", help="The output path to save the fine-tuned model data", required=True)

    args = parser.parse_args()

    print(f"JOB ID: {args.job_id}")
    print(f"MODEL NAME: {args.model_name}")
    print(f"MODEL SIZE: {args.model_size}")
    print(f"HF REPO: {args.hf_repo}")
    print(f"EPOCHS: {args.epochs}")
    print(f"LR: {args.learning_rate}")
    print(f"WR: {args.warmup_ratio}")
    print(f"PAD TOKEN: {args.pad_token}")

    print("########## LOADING THE DATA ##########")
    train_dataset = load_data(split="train", input_path=args.input_path)
    eval_dataset = load_data(split="val", input_path=args.input_path)

    print("########## LOADING THE MODEL FOR FINE-TUNING ##########")
    output_dir_path = os.path.join(args.output_path, "output", args.job_id)
    original_model, original_tokenizer, trainer = prepare_model_for_fine_tuning(output_dir_path,
                                                                                input_path=args.input_path,
                                                                                train_dataset=train_dataset,
                                                                                eval_dataset=eval_dataset,
                                                                                custom_model_name=args.hf_repo,
                                                                                epochs=int(args.epochs),
                                                                                padding_token=args.pad_token,
                                                                                learning_rate=float(args.learning_rate),
                                                                                warmup_ratio=float(args.warmup_ratio))

    print("########## START TRAINING ##########")
    target_model_dir_path = os.path.join(output_dir_path, f"{args.model_name}-{args.model_size}")
    train(original_model, trainer, target_model_dir_path)

    # print("########## LOADING FINE-TUNED MODEL ##########")
    # fine_tuned_model, tokenizer = load_fine_tuned_model(target_model_path=target_model_dir_path,
    #                                                     padding_token=args.pad_token,
    #                                                     source_model_name=args.hf_repo,
    #                                                     input_path=args.input_path)

