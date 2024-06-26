# Define variables with representative names for the numerical entities in both inputs
premise_share_Tony = 4500
hypothesis_share_Tony = 7500

# Extract all quantities as valid numbers (integers or floats)
premise_share_Tony = float(premise_share_Tony)
hypothesis_share_Tony = float(hypothesis_share_Tony)

# Use brief comments to explain what comparison you do between the defined variables
if hypothesis_share_Tony <= premise_share_Tony:
    # Check if the hypothesis value contradicts the estimate of more than 'premise_share_Tony'
    label = "contradiction"
else:
    # The premise gives only an estimate for the share of Tony
    # Any number greater than 'premise_share_Tony' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
