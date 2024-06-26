# Define variables with representative names for the numerical entities in both inputs
premise_disposable_income = 1921
hypothesis_disposable_income = 2023

# Extract all quantities as valid numbers (integers or floats)
premise_disposable_income = int(premise_disposable_income)
hypothesis_disposable_income = int(hypothesis_disposable_income)

# Use brief comments to explain what comparison you do between the defined variables
if hypothesis_disposable_income < premise_disposable_income:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
