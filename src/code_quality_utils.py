import re
import subprocess
from typing import *


def validate_code_quality(script_path):
    try:
        # Run the script using subprocess.run
        result = subprocess.run(['python', '-m', 'code_quality', '-d', script_path], capture_output=True, text=True,
                                check=True)
        evaluation = result.stdout.strip()
        # print(evaluation)
        lines = evaluation.split("\n")
        readability_score, document_size_score, redundancy_check_score, function_size_score = \
            extract_code_quality_criteria_scores(lines)
        resolutions = extract_resolutions(lines)
        return {
            "readability": readability_score,
            "document_size": document_size_score,
            "redundancy_check": redundancy_check_score,
            "function_size": function_size_score
        }, resolutions
    except subprocess.CalledProcessError as e:
        # If an exception is thrown, capture the exception information
        captured_error = e.stderr.strip()
        print(captured_error)
        return None, None


def extract_code_quality_criteria_scores(evaluation_lines: List[str]):
    readability, document_size, redundancy_check, function_size = evaluation_lines[4:8]
    readability_score = extract_score(readability)
    document_size_score = extract_score(document_size)
    redundancy_check_score = extract_score(redundancy_check)
    function_size_score = extract_score(function_size)
    return readability_score, document_size_score, redundancy_check_score, function_size_score


def extract_score(score_as_string):
    return float(re.findall(r'score\s+(\d+\.\d+)', score_as_string.lower().split(" / ")[0])[0])


def extract_resolutions(evaluation_lines: List[str]):
    resolutions = []
    for line in evaluation_lines[9:]:
        if line.startswith("-"):
            resolutions.append(line.split("> ")[-1])
    return resolutions
