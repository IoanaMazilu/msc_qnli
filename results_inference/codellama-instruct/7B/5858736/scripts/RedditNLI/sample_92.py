import re

# Extract the numerical entities from the input sentences
premise_amount = re.findall(r'\d+', premise)[0]
hypothesis_amount = re.findall(r'\d+', hypothesis)[0]

# Convert the numerical entities to integers
premise_amount = int(premise_amount)
hypothesis_amount = int(hypothesis_amount)

# Check if the amounts in the hypothesis contradict the amount in the premise
if hypothesis_amount!= premise_amount:
    label = "contradiction"
else:
    # If the amounts in the hypothesis and premise are equal, we can infer entailment
    label = "entailment"

print(label)
