import re

def extract_numbers(sentence):
    return [float(x) for x in re.findall(r'[0-9]+[.]?[0-9]*', sentence)]
