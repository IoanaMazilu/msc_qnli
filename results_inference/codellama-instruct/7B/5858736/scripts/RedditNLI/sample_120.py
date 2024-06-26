# Define variables with representative names for the numerical entities in both inputs
base_rate_premise = 2006
base_rate_hypothesis = 2008

# Extract all quantities as valid numbers (integers or floats)
base_rate_premise = int(base_rate_premise)
base_rate_hypothesis = int(base_rate_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if base_rate_hypothesis > base_rate_premise:
    # Check if the base rate in the hypothesis is greater than the base rate in the premise
    label = "entailment"
else:
    # If the base rate in the hypothesis is not greater than the base rate in the premise, we can infer contradiction
    label = "contradiction"

print(label)
