import time
import traceback

# from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, logging

from prompts import format_prompt


def load_model(model_name: str = None):
    """
    Loads a HF quantized model (with GPTQ)
    :param model_name: the HF model path as `repo/model_name`
    :return: a model and a tokenizer object
    """
    assert "llama" in model_name.lower() or "mistral" in model_name.lower()
    model_name_or_path = model_name if model_name else "TheBloke/CodeLlama-13B-Python-GPTQ"
    model_basename = "model"
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

    model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
                                                 device_map="cuda:0",
                                                 trust_remote_code=True,
                                                 revision="main")
    # model = AutoGPTQForCausalLM.from_quantized(model_name_or_path,
    #                                            model_basename=model_basename,
    #                                            use_safetensors=True,
    #                                            trust_remote_code=True,
    #                                            device="cuda:0",
    #                                            # use_triton=use_triton,
    #                                            # quantize_config=None,
    #                                            revision="main")
    # Prevent printing spurious transformers error when using pipeline with AutoGPTQ
    logging.set_verbosity(logging.CRITICAL)
    return model, tokenizer


def get_inference_pipeline(model, tokenizer, **kwargs):
    return pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=kwargs.get("max_new_tokens", 512),
        do_sample=True,
        temperature=kwargs.get("temperature", 0.7),
        top_p=kwargs.get("top_p", 0.95),
        top_k=kwargs.get("top_k", 40),
        repetition_penalty=kwargs.get("repetition_penalty", 1.1)
    )


print(f"GPU available: {torch.cuda.is_available()}")

input_sample = {
    "premise": "Sam had 9.0 dimes in his bank  and his dad gave him 7.0 dimes",
    "hypothesis": "Sam has 16.0 dimes now"
}

prompt = format_prompt(prompt_type="awpnli", input_sample=input_sample)
# print(f"########## PROMPT ##########\n{prompt}")

for model_name in ["TheBloke/CodeLlama-7B-Python-GPTQ",
                   "TheBloke/CodeLlama-13B-Python-GPTQ",
                   # "TheBloke/Llama-2-7B-GPTQ",
                   # "TheBloke/Llama-2-13B-GPTQ",
                   "TheBloke/Mistral-7B-Instruct-v0.2-GPTQ"
                   ]:
    print(f"########## USING {model_name.split('/')[1]}")
    try:
        model, tokenizer = load_model(model_name)
        inference_pipe = get_inference_pipeline(model, tokenizer)
        start = time.time()
        response = inference_pipe(prompt)
        end = time.time()
        text = response[0]["generated_text"].rpartition("Answer:")[-1].replace("```", "")
        print(f"########## COMPLETION ##########\n{text}")
        print(f"########## DURATION ##########\n{(end - start) / 60:.2f} min")
    except:
        print(f"########## ERROR ##########\n{traceback.print_exc()}")



