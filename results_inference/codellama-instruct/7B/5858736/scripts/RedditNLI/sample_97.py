import re

# Extract the numerical values from the input sentences
premise_num = re.findall(r'\d+', premise)
hypothesis_num = re.findall(r'\d+', hypothesis)

# Convert the numerical values to integers
premise_num = int(premise_num[0])
hypothesis_num = int(hypothesis_num[0])

# Check if the hypothesis contradicts the premise
if hypothesis_num > premise_num:
    label = "contradiction"
else:
    label = "neutral"

print(label)
