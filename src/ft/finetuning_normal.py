# !pip install -q accelerate==0.21.0 peft==0.4.0 bitsandbytes==0.40.2 transformers==4.31.0 trl==0.4.7
import argparse
import os
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


def load_data(dataset: str, split: str, input_path: str = None):
    data_directory_path = input_path if input_path else os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "data")
    return load_dataset('csv',
                        data_files=os.path.join(data_directory_path,
                                                "input",
                                                f'{split}_text.csv'))


def prepare_model_for_fine_tuning(custom_output_dir: str,
                                  train_dataset=None,
                                  eval_dataset=None,
                                  custom_model_name: str = None):
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
        device_map=device_map
    )
    model.config.use_cache = False
    model.config.pretraining_tp = 1
    print(f"Model loaded in {round((time.time() - start_time)/60, 2)} min.")

    # Load LLaMA tokenizer
    print("Loading the tokenizer...")
    start_time = time.time()
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"  # Fix weird overflow issue with fp16 training
    print(f"Tokenizer loaded in {round((time.time() - start_time) / 60, 2)} min.")

    # Load LoRA configuration
    peft_config = LoraConfig(
        lora_alpha=lora_alpha,
        lora_dropout=lora_dropout,
        r=lora_r,
        bias="none",
        task_type="CAUSAL_LM",
    )

    # Set training parameters
    training_arguments = TrainingArguments(
        output_dir=custom_output_dir,
        num_train_epochs=num_train_epochs,
        per_device_train_batch_size=per_device_train_batch_size,
        gradient_accumulation_steps=gradient_accumulation_steps,
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
        report_to=["tensorboard"]
    )

    response_template = " ### Response:\n"
    collator = DataCollatorForCompletionOnlyLM(response_template, tokenizer=tokenizer, mlm=False)

    # Set supervised fine-tuning parameters
    trainer = SFTTrainer(
        model=model,
        train_dataset=train_dataset if train_dataset else load_dataset(dataset_name),
        eval_dataset=eval_dataset,
        peft_config=peft_config,
        # dataset_text_field="text",
        max_seq_length=max_seq_length,
        tokenizer=tokenizer,
        args=training_arguments,
        packing=packing,
        data_collator=collator,
    )
    return model, trainer


# Train model
def train(model, trainer, target_model_name):
    trainer.train()

    # Save trained model
    print("Saving fine-tuned model...")
    trainer.model.save_pretrained(target_model_name)

    # Empty VRAM
    del model
    del trainer
    import gc
    gc.collect()
    gc.collect()


def load_fine_tuned_model(target_model_name: str, source_model_name: str = None):
    # Reload model in FP16 and merge it with LoRA weights
    base_model = AutoModelForCausalLM.from_pretrained(
        source_model_name if source_model_name else model_name,
        low_cpu_mem_usage=True,
        return_dict=True,
        torch_dtype=torch.float16,
        device_map=device_map,
    )
    try:
        ft_model = PeftModel.from_pretrained(base_model, os.path.join(output_dir, target_model_name))
        print("PEFT Model needs path to saved fine-tuned model")
    except Exception:
        print(traceback.print_exc())
        print("####################\nPEFT Model needs only fine-tuned model name")
        ft_model = PeftModel.from_pretrained(base_model, target_model_name)
    ft_model = ft_model.merge_and_unload()

    # Reload tokenizer to save it
    tokenizer = AutoTokenizer.from_pretrained(source_model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    return ft_model, tokenizer


def inference_with_fine_tuned_model(model, tokenizer):
    # Ignore warnings
    logging.set_verbosity(logging.CRITICAL)
    # Run text generation pipeline with our next model
    prompt = "### Instruction:\nYou need to reason about weather a hypothesis entails or contradicts a premise, by generating Python scripts. The scripts should classify the relation between the hypothesis and premise based on the quantitative and textual information mentioned in them. All the quantities and textual details in the hypothesis should be entailed by the information in the premise. First, manually extract all the individual quantities from both of the inputs, as valid numbers. Use the variable name to describe what the quantity measures, based on the context. Then, define a Python function that takes the extracted quantities as arguments. Within the function, use these quantities to perform computations based on the context of the premise and hypothesis. Finally, compare the resulting variables to determine the relationship. If the comparison indicates entailment, return True; for contradiction return False. Remember to include brief comments in the script to explain each step of the reasoning process. To illustrate, consider the following examples:\nSTART_EXAMPLE\nPremise: Yesterday I learned 35 verbs and 5 nouns in the morning and 10 verbs in the evening.\nHypothesis: I learned 5 nouns and less than fifty verbs yesterday.\nAnswer:\n```python\nverbs_morning_premise = 35\nverbs_evening_premise = 10\nnouns_premise = 5\nmax_verbs_hypothesis = 50 \nnouns_hypothesis = 5\n\ndef entailment_or_contradiction(verbs_morning_premise, verbs_evening_premise, nouns_premise, max_verbs_hypothesis, nouns_hypothesis):\n    # the hypothesis talks about the number of learned nouns and verbs, which are also referenced in the premise\n    # find the total number of verbs learned from the premise \n    total_verbs_premise = verbs_morning_premise + verbs_evening_premise\n    # check if the total verbs form the hypothesis is more than 'verbs_evening_premise' and if the number of nouns is equal between the premise and hypothesis\n    return max_verbs_hypothesis > total_verbs_premise and nouns_premise == nouns_hypothesis\n\nprint(entailment_or_contradiction(verbs_morning_premise, verbs_evening_premise, nouns_premise, max_verbs_hypothesis, nouns_hypothesis))\n```\nEND_EXAMPLE\n\nSTART_EXAMPLE\nPremise: She bought 10 crayons and received 5 more from her desk mate.\nHypothesis: She has 10 crayons in total.\nAnswer:\n```python\nbought_crayons_premise = 10\nreceived_crayons_premise = 5\ntotal_crayons_hypothesis = 12\n\ndef entailment_or_contradiction(bought_crayons_premise, received_crayons_premise, total_crayons_hypothesis):\n    # the entity in the hypothesis can be computed from the entities in the premise\n    total_crayons_premise = bought_crayons_premise + received_crayons_premise\n    # check if 'total_crayons_hypothesis' entails the quantity deduced from the premise, so if they are equal\n    return total_crayons_premise == total_crayons_hypothesis:\n\nprint(entailment_or_contradiction(bought_crayons_premise, received_crayons_premise, total_crayons_hypothesis))\n```\nEND_EXAMPLE\n### Input:\nPremise: Sally had 760.0 quarters in her bank  and she spent 418.0 of her quarters \nHypothesis: She has 342.0 quarters now\n### Response:\n"
    expected_response = "```python\nquarters_beginning_premise = 760.0\nquarters_spent_premise = 418.0\nquarters_remaining_hypothesis = 342.0\n\ndef entailment_or_contradiction(quarters_beginning_premise, quarters_spent_premise, quarters_remaining_hypothesis):\n    # the hypothesis talks about the remaining quarters, which can be computed from the premise\n    quarters_remaining_premise = quarters_beginning_premise - quarters_spent_premise\n    # check if 'quarters_remaining_hypothesis' entails the quantity deduced from the premise, so if they are equal\n    return quarters_remaining_premise == quarters_remaining_hypothesis\n\nprint(entailment_or_contradiction(quarters_beginning_premise, quarters_spent_premise, quarters_remaining_hypothesis))\n```"
    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=512)
    result = pipe(f"<s>[INST] {prompt} [/INST]")
    print("INFERENCE WITH FINE-TUNED MODEL:\n")
    print(f"PROMPT: {prompt}")
    print(f"COMPLETION: {result[0]['generated_text']}")
    print(f"EXPECTED COMPLETION: {expected_response}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='QNLI prediction')
    parser.add_argument('-e', '--experiment', required=True, help="The name of the experiment")
    parser.add_argument('-d', '--dataset', choices=["AWPNLI", "NewsNLI", "RedditNLI", "RTE_Quant", "StressTest"],
                        required=False, help="The name of the dataset used in the experiment.")
    parser.add_argument('-s', '--source-model', default="meta-llama/Llama-2-7b-hf",
                        required=False, help="The name of the HF model to be fine-tuned.")
    parser.add_argument('-t', "--target_model", required=True, help="The name of the fine-tuned model")
    parser.add_argument("-i", "--input-path", help="The path to the datasets", required=False)
    parser.add_argument("-o", "--output-path", help="The output path to save the fine-tuned model data", required=True)

    args = parser.parse_args()

    output_dir = os.path.join(args.output_path, "output", args.experiment)
    ds = args.dataset

    print("########## LOADING THE DATA ##########")
    train_dataset = load_data(dataset=ds, split="train", input_path=args.input_path)
    eval_dataset = load_data(dataset=ds, split="val", input_path=args.input_path)

    print("########## LOADING THE MODEL FOR FINE-TUNING ##########")
    model, trainer = prepare_model_for_fine_tuning(output_dir, train_dataset)

    print("########## START TRAINING ##########")
    train(model, trainer, args.target_model)

    print("########## LOADING FINE-TUNED MODEL ##########")
    fine_tuned_model, tokenizer = load_fine_tuned_model(args.target_model, args.source_model)

    print("########## TESTING MODEL FOR INFERENCE ##########")
    inference_with_fine_tuned_model(fine_tuned_model, tokenizer)
