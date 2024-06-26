# Define variables with representative names for the numerical entities in both inputs
premise_earnings = 9000
hypothesis_earnings = 4000

# Extract all quantities as valid numbers (integers or floats)
premise_earnings = int(premise_earnings)
hypothesis_earnings = int(hypothesis_earnings)

# Use brief comments to explain what comparison you do between the defined variables
if hypothesis_earnings <= premise_earnings:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # If the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"

print(label)
