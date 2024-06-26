# Define variables with representative names for the numerical entities in both inputs
amount_withdrawn_premise = 5000
amount_withdrawn_hypothesis = 2000

# Extract all quantities as valid numbers (integers or floats)
amount_withdrawn_premise = int(amount_withdrawn_premise)
amount_withdrawn_hypothesis = int(amount_withdrawn_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if amount_withdrawn_hypothesis <= amount_withdrawn_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'amount_withdrawn_premise'
    label = "contradiction"
else:
    # The hypothesis value is greater than the estimate of less than 'amount_withdrawn_premise'
    # Any number greater than 'amount_withdrawn_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
