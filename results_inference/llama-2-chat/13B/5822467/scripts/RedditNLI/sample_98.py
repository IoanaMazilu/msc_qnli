# Define variables with representative names for the numerical entities in both inputs
saudi_central_bank_net_foreign_assets_premise = 1.0
saudi_central_bank_net_foreign_assets_hypothesis = -6

# Extract all quantities as valid numbers (integers or floats)
saudi_central_bank_net_foreign_assets_premise = float(saudi_central_bank_net_foreign_assets_premise)
saudi_central_bank_net_foreign_assets_hypothesis = float(saudi_central_bank_net_foreign_assets_hypothesis)

# Compare the variables
if saudi_central_bank_net_foreign_assets_hypothesis!= saudi_central_bank_net_foreign_assets_premise:
    # Check if the hypothesis contradicts the premise
    label = "contradiction"
elif saudi_central_bank_net_foreign_assets_hypothesis < saudi_central_bank_net_foreign_assets_premise:
    # Check if the hypothesis value is less than the premise value
    label = "entailment"
else:
    # The hypothesis value is greater than or equal to the premise value, so the label is neutral
    label = "neutral"

# Print the label
print(label)
