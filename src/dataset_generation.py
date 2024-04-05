import re
import random
import time
import pandas as pd
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from qnli_datasets import read_data
from prompts import get_prompt, python_script_template
from sklearn.metrics import classification_report
import argparse
import os
from utils import run_script
import logging

load_dotenv()


# def init_logger(experiment_name: str, dataset: str, prompt_type: str, model: str, **kwargs):
#     test_logger = logging.getLogger(f"{experiment_name}_logger")
#     test_logger.setLevel(logging.DEBUG)
#     root_path = os.path.dirname(os.getcwd())  # path to parent directory of current directory
#     results_path = os.path.join(root_path, "results", dataset.lower(), experiment_name)
#     f_handler = logging.FileHandler(os.path.join(results_path, f"{experiment_name}.log"))
#     f_handler.setLevel(logging.DEBUG)
#     test_logger.addHandler(f_handler)
#     return test_logger


def get_llm(model_name: str, **kwargs):
    # available gpt4 engines: gpt-4, gpt-4-0613, gpt-4-32k, gpt-4-32k-0613
    temperature = kwargs.get('temperature', 0.7)
    if model_name in ["gpt-3.5-turbo", "gpt-4", "gpt-3.5-turbo-1106"]:
        # other params: openai_api_base, openai_organization
        return ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY_UVA"),
                          model_name=model_name,
                          temperature=temperature)


def make_chain(llm_model_name: str, prompt_type: str, **llm_kwargs) -> LLMChain:
    llm = get_llm(llm_model_name, **llm_kwargs)
    prompt = get_prompt(prompt_type)
    return LLMChain(prompt=prompt, llm=llm, verbose=False)


def generate_labels(model: str,
                    dataset: str,
                    experiment_name: str,
                    random_samples: bool,
                    samples_count: int,
                    verbose: bool = None,
                    output_path: str = None,
                    **llm_kwargs):
    """
    Generates Python scripts in a CoT style for the samples in the givn dataset, using the specified OpenAI model.
    The scripts are saved to "data/generated/{dataset}/{experiment_name}", together with a CSV-overview of the
    LLM responses.
    :param model: an OpenAI model (gpt3.5-turbo or gpt4)
    :param dataset: one of the 5 datasets inside EQUATE
    :param experiment_name: a name for the dataset generation experiment
    :param verbose: not used
    :param llm_kwargs: not used
    :return:
    """
    root_path = os.path.dirname(os.getcwd())
    input_path = os.path.join(root_path, "data", "equate", "03_cleaned", f"{dataset}.csv")
    if not output_path:
        output_path = os.path.join(root_path, "data", "generated", dataset, experiment_name)
        code_quality_output_path = os.path.join(root_path, "data", "code_quality", "gpt4", dataset, experiment_name)
        os.makedirs(output_path, exist_ok=True)
        os.makedirs(code_quality_output_path, exist_ok=True)

    chain = make_chain(model, f"{dataset.lower().replace('_', '')}", **llm_kwargs)

    answers, py_file_contents = [], []
    samples = pd.read_csv(input_path).set_index("sample_index")
    labels = list(samples["label"].unique())
    # select random subset of `samples_count` or 10% of the samples in the dataset
    if samples_count == 0:
        subset_idx = list(range(len(samples)))
    else:
        random_sample_size = samples_count if samples_count else int(len(samples) * 0.1)
        subset_idx = list(range(samples_count)) if not random_samples else random.sample(range(0, len(samples)), random_sample_size)
    # subset_idx = [5345, 750, 2301, 5100, 4534, 5217, 4237, 1892, 5001, 792, 4744, 3166, 3722, 5382, 3297, 1644, 5870, 2324, 1782, 2099, 2862, 6148, 454, 5614, 3267, 2093, 6994, 403, 3537, 652, 5272, 2045, 5252, 4233, 4256, 1140, 3864, 596, 2424, 5900, 3440, 4643, 6324, 4206, 176, 3107, 1083, 5079, 1579, 4481]
        print(subset_idx)
    # get indices of samples for which data was already generated
    try:
        previous_results = pd.read_csv(os.path.join(output_path, "results_overview.csv"))
        skip_indices = previous_results["sample_index"].unique()
    except FileNotFoundError:
        previous_results = None
        skip_indices = []
    print(f"Sampled indices:\n{subset_idx}")

    samples_in_batch = 0
    processed_indices = []
    try:
        for idx in subset_idx:
            if idx in skip_indices:
                print(f"Skipping index {idx}")
                continue
            processed_indices.append(idx)
            samples_in_batch += 1

            llm_answer, py_file_content, script = get_label_for_sample(chain, samples.loc[idx], labels)
            if py_file_content:
                save_python_script_to_file(output_path, py_file_content, idx)
                save_python_script_to_file(code_quality_output_path, script, idx)
            if llm_answer is None:
                llm_answer, py_file_content = "-", "-"
            answers.append(llm_answer)
            py_file_contents.append(py_file_content)

            if samples_in_batch == 30:
                # use batches of 30 to not exceed openai model token limit (tpm)
                print("Batch completed, waiting...")
                samples_in_batch = 0
                time.sleep(5)
    finally:
        overview_df = pd.DataFrame(data={
            "sample_index": processed_indices[:len(answers)],
            "llm_answer": answers,
            "py_file_content": py_file_contents
        })
        if previous_results is not None:
            # add results to previous results
            try:
                overview_df = pd.concat([previous_results, overview_df], axis=0, ignore_index=True)
            except:
                overview_df.to_csv(os.path.join(output_path, "results_overview_new.csv"), index=False)
                return
        overview_df.to_csv(os.path.join(output_path, "results_overview.csv"), index=False)


def save_python_script_to_file(output_path: str, script_str: str, idx: int) -> None:
    """
    Writes the given python script to a new or existing .py file, at the output path.
    :param output_path: the directory where the .py files are created
    :param script_str: the script to be written to the .py file
    :param idx: the index from the dataset of the sample to which the script is associated
    """
    try:
        with open(os.path.join(output_path, f"sample_{idx}.py"), "x") as f:
            f.write(script_str)
    except FileExistsError:
        with open(os.path.join(output_path, f"sample_{idx}.py"), "w") as f:
            f.write(script_str)


def get_label_for_sample(chain, sample, potential_labels):
    """
    Generate a Python script for the given sample.
    :param chain: a langchain LLM chain with a prompt
    :param sample: a pair of premise-hypothesis and the ground-truth label
    :param potential_labels: the unique labels in the originating dataset of the given samples
    :return:
    """
    premise, hypothesis, golden_label = sample['premise'], sample['hypothesis'], sample['label']
    try:
        answer = chain.run({'premise': premise, 'hypothesis': hypothesis})  # , 'labels': potential_labels
    except Exception as e:
        print(e)
        return None, None
    code_extraction_regex, code_extraction_regex_backup = r"```python([^`]+)```", r"`python([^`]+)`"
    scripts = re.findall(code_extraction_regex, answer)
    if not scripts:
        # rare case: max_tokens reached before "```" indicator is completely returned by LLM
        scripts = re.findall(code_extraction_regex_backup, answer)
        if not scripts:
            # max_tokens reached before the code is fully generated or the llm did not generate a block of code at all
            print("No Python script found in text.")
            return answer, None
    script = "\n".join(scripts).replace("`", "").lstrip("\n")  # collect all scripts, if more are returned
    runnable_py_file_template = python_script_template.replace("{premise}", premise.replace("\n", " ")) \
        .replace("{hypothesis}", hypothesis.replace("\n", " ")). \
        replace("{label}", golden_label). \
        replace("{script}", script)
    return answer, runnable_py_file_template, script


def extract_labels_from_scripts(dataset: str, experiment_name: str) -> None:
    """
    Extract the labels from the generated scripts for the samples in the given dataset, under the
    given experiment.
    :param dataset: one of the 5 datasets in EQUATE
    :param experiment_name: the name of the experiment under which the labels were generated
    """
    results = []
    root_path = os.path.dirname(os.getcwd())
    output_path = os.path.join(root_path, "data", "equate_labelled")
    os.makedirs(output_path, exist_ok=True)
    input_path = os.path.join(root_path, "data", "generated", dataset, experiment_name)
    try:
        previous_results = pd.read_csv(os.path.join(output_path, f"{dataset}_{experiment_name}.csv"))
        skip_indices = previous_results["sample_index"].unique()  # do not re-process current results
    except FileNotFoundError:
        previous_results = None
        skip_indices = []
    try:
        for f in os.listdir(input_path):
            if f.endswith(".py"):
                idx = f.split(".")[0].split("_")[-1]  # extract the sample index from the script file name
                if not idx in skip_indices:
                    label, info = run_script(os.path.join(input_path, f))
                    results.append({"sample_index": idx, "generated_label": label, "error_message": info})
    except Exception as e:
        print(e)
    finally:
        results_df = pd.DataFrame(results)
        if previous_results is not None:
            results_df = pd.concat([previous_results, results_df], axis=0, ignore_index=True)
        results_df.to_csv(os.path.join(output_path, f"{dataset}_{experiment_name}.csv"), index=False)


def validate_generated_labels(dataset, experiment_name):
    samples, _ = read_data(dataset + ".jsonl")
    root_path = os.path.dirname(os.getcwd())
    generated_data_path = os.path.join(root_path, "data", "equate_labelled")
    generated_labels = pd.read_csv(os.path.join(generated_data_path, f"{dataset}_{experiment_name}.csv"))
    generated_labels["golden_label"] = generated_labels["sample_index"].apply(lambda idx: samples[idx]['label'])
    generated_labels["premise"] = generated_labels["sample_index"].apply(lambda idx: samples[idx]['premise'])
    generated_labels["hypothesis"] = generated_labels["sample_index"].apply(lambda idx: samples[idx]['hypothesis'])
    generated_labels.to_csv(os.path.join(generated_data_path, f"{dataset}_{experiment_name}.csv"), index=False)
    print(f"CLASSIFICATION REPORT FOR DATASET {dataset} (exp. {experiment_name})")
    valid_results = generated_labels[generated_labels['error_message'].isna()]
    print(classification_report(y_true=valid_results['golden_label'],
                                y_pred=valid_results['generated_label']))
    misclassified_samples = list(
        valid_results[valid_results['golden_label'] != valid_results['generated_label']]['sample_index'].unique())
    print(f"Misclassified samples: {sorted(misclassified_samples)}")
    invalid_samples = list(generated_labels[generated_labels['error_message'].notna()]['sample_index'].unique())
    print(f"Invalid samples: {sorted(invalid_samples)}")


if __name__ == "__main__":
    for dataset in ["AWPNLI", "RedditNLI", "NewsNLI", "RTE_Quant", "StressTest"]:
        print(f"############{dataset}############")
        experiment_name = "phase2-test"
        # GENERATE SCRIPTS FOR THE QNLI TASK
        start_time = time.time()
        generate_labels(model="gpt-4", dataset=dataset,
                        experiment_name=experiment_name,
                        samples_count=50,
                        random_samples=True,
                        verbose=True)
        print(f"Finished script generation in {round(time.time() - start_time, 2)} seconds.")

    # EXTRACT THE LABELS BASED ON THE SCRIPT RETURN VALUE
    # extract_labels_from_scripts(dataset, experiment_name)
    # EVALUATE THE CLASSIFICATION RESULTS
    # validate_generated_labels(dataset, experiment_name)

    # chain4 = make_chain("gpt-4", "stresstest")
    # chain35 = make_chain("gpt-3.5-turbo-1106", "stresstest")
    # example = {"premise": "Tim has 350 pounds of cement in 100 , 50 , and 25 pound bags",
    #            "hypothesis": "Tim has less than 350 pounds of cement in 100 , 50 , and 25 pound bags",
    #            "label": "neutral"}
    # _, scr = get_label_for_sample(chain35, example, [])
    # print(scr)
    #
    # _, scr = get_label_for_sample(chain4, example, [])
    # print(scr)
