# CODE SOURCE: https://gist.github.com/SunMarc/dcdb499ac16d355a8f265aa497645996
# coding=utf-8
# Copyright 2023 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
# from dataclasses import dataclass, field
# from typing import Optional

from datasets import load_dataset
from peft import (LoraConfig,
                  prepare_model_for_kbit_training,
                  get_peft_model)
import torch
from transformers import (AutoModelForCausalLM,
                          AutoTokenizer,
                          GPTQConfig,
                          # HfArgumentParser,
                          TrainingArguments)
from trl import DataCollatorForCompletionOnlyLM, SFTTrainer

# This example fine-tunes Llama 2 model on Guanaco dataset
# using GPTQ and peft.
# Use it by correctly passing --model_name argument when running the
# script. The default model is ybelkada/llama-7b-GPTQ-test

# Versions used:
# accelerate == 0.21.0
# auto-gptq == 0.4.2
# trl == 0.4.7
# peft from source
# transformers from source
# optimum from source

# For models that have `config.pretraining_tp > 1` install:
# pip install git+https://github.com/huggingface/transformers.git


def load_data(split: str):
    data_directory_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "data")
    return load_dataset('json',
                        data_files=os.path.join(data_directory_path,
                                                "finetuning",
                                                "AWPNLI"
                                                f'{split}.json'))


def create_and_prepare_model(model_name: str = None, args=None):
    model_name = model_name if model_name else "TheBloke/CodeLlama-7B-Python-GPTQ"
    major, _ = torch.cuda.get_device_capability()
    if major >= 8:
        print("=" * 10)
        print("Your GPU supports bfloat16, you can accelerate training with the argument --bf16")
        print("=" * 10)

    # Load the entire model on the GPU 0
    device_map = {"": 0}
    # switch to `device_map = "auto"` for multi-GPU
    # device_map = "auto"

    # need to disable exllama kernel
    # exllama kernel are not very stable for training
    model = AutoModelForCausalLM.from_pretrained(
        model_name,  #args.model_name,
        device_map=device_map,
        quantization_config=GPTQConfig(bits=4, disable_exllama=True)
    )

    # check: https://github.com/huggingface/transformers/pull/24906
    model.config.pretraining_tp = 1

    peft_config = LoraConfig(
        lora_alpha=16,  #script_args.lora_alpha,
        lora_dropout=0.1,  # script_args.lora_dropout,
        r=64,  # script_args.lora_r,
        bias="none",
        task_type="CAUSAL_LM",
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token

    return model, peft_config, tokenizer


training_arguments = TrainingArguments(
    output_dir="./results",  # script_args.output_dir,
    per_device_train_batch_size=4,  # script_args.per_device_train_batch_size,
    gradient_accumulation_steps=4,  # script_args.gradient_accumulation_steps,
    optim="adamw_hf",  # script_args.optim,
    save_steps=10,  # script_args.save_steps,
    logging_steps=10,  # script_args.logging_steps,
    learning_rate=2e-4,  # script_args.learning_rate,
    fp16=False,  # script_args.fp16,
    bf16=True,  # script_args.bf16,
    max_grad_norm=0.3,  # script_args.max_grad_norm,
    max_steps=10000,  # script_args.max_steps,
    warmup_ratio=0.03,  # script_args.warmup_ratio,
    group_by_length=True,  # script_args.group_by_length,
    lr_scheduler_type="constant"  # script_args.lr_scheduler_type,
)

model, peft_config, tokenizer = create_and_prepare_model()
model = prepare_model_for_kbit_training(model)
model = get_peft_model(model, peft_config)
model.config.use_cache = False
train_dataset = load_data(split="train")   # load_dataset(script_args.dataset_name, split="train")
eval_dataset = load_data(split="val")

instruction_template = "### Human:"
response_template = "### Assistant:"
collator = DataCollatorForCompletionOnlyLM(instruction_template=instruction_template, response_template=response_template, tokenizer=tokenizer, mlm=False)

# Fix weird overflow issue with fp16 training
tokenizer.padding_side = "right"
trainer = SFTTrainer(
    model=model,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    dataset_text_field="text",
    max_seq_length=4096,  # script_args.max_seq_length,
    tokenizer=tokenizer,
    args=training_arguments,
    packing=True  # script_args.packing,
)

trainer.train()

merge_and_push = True

if merge_and_push:
    output_dir = os.path.join("./results", "final_checkpoints")
    trainer.model.save_pretrained(os.path.join(output_dir, "model"))
    tokenizer.save_pretrained(os.path.join(output_dir, "tokenizer"))
    # Free memory for merging weights
    del model
    torch.cuda.empty_cache()
