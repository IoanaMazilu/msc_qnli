import re

def extract_numbers(sentence):
    return [int(x) for x in re.findall(r'\d+', sentence)]
