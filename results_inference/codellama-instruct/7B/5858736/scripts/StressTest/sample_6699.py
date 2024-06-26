# Define variables with representative names for the numerical entities in both inputs
premise_share_Tony = 4500
hypothesis_share_Tony = 6500

# Extract all quantities as valid numbers (integers or floats)
premise_share_Tony = float(premise_share_Tony)
hypothesis_share_Tony = float(hypothesis_share_Tony)

# Use brief comments to explain what comparison you do between the defined variables
if hypothesis_share_Tony <= premise_share_Tony:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis value is greater than the premise, we can infer entailment
    label = "entailment"

print(label)
