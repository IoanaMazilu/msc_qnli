import pandas as pd
import os
import jsonlines
from typing import List, Set, Literal


def read_data(filename: str = None, labels: List[str] | str = None) -> (List[dict], Set[str]):
    """
    Reads a jsonl file containing samples for the QNLI task.
    :param filename: name of file to be read
    :param labels: one or more labels used as filters for the returned samples
    :return: a list of QNLI samples in dict format with keys 'premise', 'hypothesis', 'label' and a set of the labels
    in this dataset.
    """
    if labels and isinstance(labels, str):
        labels = [labels]
    samples = []
    data_path = os.path.join("../data", "equate")
    with jsonlines.open(os.path.join(data_path, filename)) as reader:
        for sample in reader:
            if labels is None or sample['gold_label'] in labels:  # we are only interested in entailment/contradiction
                samples.append(sample)
    # extract only premise, hypothesis and label
    samples = [{new_key: sample[old_key] for new_key, old_key in
               zip(['premise', 'hypothesis', 'label'], ['sentence1', 'sentence2', 'gold_label'])}
               for sample in samples]
    labels = set([sample['label'] for sample in samples]) if not labels else labels  # unique labels
    return samples, labels


def sample_examples(data: List[dict],
                    labels: Set[str] = None,
                    n: int = 3,
                    how: str = Literal["random", "diverse"]) -> List[dict]:
    """
    Samples examples from a dataset, according to a sampling strategy.
    :param data: a list of samples in dict format
    :param labels: a set of the labels in the dataset
    :param n: the number of samples to be sampled
    :param how: how to sample the examples. 'random' sampling will return `n` samples without accounting for the label.
    'diverse` strategy will sample one example for each label and then random examples until `n` examples are chosen
    in total. If there are more labels than `n`, only up to 'n' diverse labels will be sampled.
    :return: a list of samples in dict format
    """
    pass


if __name__ == "__main__":
    for dataset in ["AWPNLI", "RedditNLI", "NewsNLI", "RTE_Quant", "StressTest"]:
        print(dataset)
        samples, _ = read_data(f"{dataset}.jsonl")
        df = pd.DataFrame(samples)
        df["sample_index"] = df.index
        print(df.shape[0])
        df.to_csv(os.path.join("../data", "equate", f"{dataset}.csv"), index=False)

