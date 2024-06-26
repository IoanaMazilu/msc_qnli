# Define variables with representative names for the numerical entities in both inputs
amount_wanted_premise = 95
amount_wanted_hypothesis = 55

# Extract all quantities as valid numbers (integers or floats)
amount_wanted_premise = float(amount_wanted_premise)
amount_wanted_hypothesis = float(amount_wanted_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if amount_wanted_hypothesis <= amount_wanted_premise:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the amount wanted
    # Any amount greater than 'amount_wanted_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
