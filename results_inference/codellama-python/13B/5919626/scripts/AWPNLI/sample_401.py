import re

def extract_numbers(sentence):
    return [float(x) for x in re.findall(r'(\d+\.\d+|\d+)', sentence)]
