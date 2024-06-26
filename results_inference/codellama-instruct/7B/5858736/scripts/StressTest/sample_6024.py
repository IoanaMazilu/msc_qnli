# Define variables with representative names for the numerical entities in both inputs
amount = 4
percentage = 6

# Extract all quantities as valid numbers (integers or floats)
amount = float(amount)
percentage = float(percentage)

# Use brief comments to explain what comparison you do between the defined variables
if percentage < amount:
    # Check if the hypothesis value contradicts the estimate of less than 'percentage'
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
