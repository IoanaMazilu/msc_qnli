import re

def extract_numbers(text):
    return [float(x) for x in re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', text)]
