# Define variables with representative names for the numerical entities in both inputs
discount_premise = 288
discount_hypothesis = 588

# Extract all quantities as valid numbers (integers or floats)
discount_premise = float(discount_premise)
discount_hypothesis = float(discount_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if discount_hypothesis < discount_premise:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
