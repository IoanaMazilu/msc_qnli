# Define variables with representative names for the numerical entities in both inputs
amount_premise = 10000
amount_hypothesis = 10000

# Extract all quantities as valid numbers (integers or floats)
amount_premise = float(amount_premise)
amount_hypothesis = float(amount_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if amount_hypothesis!= amount_premise:
    # Check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
