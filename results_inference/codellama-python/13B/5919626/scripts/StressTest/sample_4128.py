import re

def extract_numbers(text):
    return [int(s) for s in re.findall(r'\d+', text)]
