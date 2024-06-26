# Define variables with representative names for the numerical entities in both inputs
premise_pay = 150
hypothesis_pay = 150

# Extract all quantities as valid numbers (integers or floats)
premise_pay = int(premise_pay)
hypothesis_pay = int(hypothesis_pay)

# Use brief comments to explain what comparison you do between the defined variables
if hypothesis_pay >= premise_pay:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # If the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
