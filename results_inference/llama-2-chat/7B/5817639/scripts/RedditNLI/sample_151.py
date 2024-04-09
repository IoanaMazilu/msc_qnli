import math

# Define variables for the premise and hypothesis
premise_price_drop = 0
hypothesis_price_drop = 0

# Extract quantities from the premise and hypothesis
premise_quantity = float(input_premise.split(" ")[1])
hypothesis_quantity = float(input_hypothesis.split(" ")[1])

# Check if the quantity in the hypothesis contradicts the quantity in the premise
if hypothesis_quantity < premise_quantity:
    label = "contradiction"
else:
    # Check if the quantity in the hypothesis is consistent with the quantity in the premise
    if hypothesis_quantity >= premise_quantity:
        label = "entailment"
    else:
        label = "neutral"

# Print the label
print(label)
