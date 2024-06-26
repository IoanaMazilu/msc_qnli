# Define variables with representative names for the numerical entities in both inputs
profit_premise = 6970
profit_hypothesis = 1970

# Extract all quantities as valid numbers (integers or floats)
profit_premise = int(profit_premise)
profit_hypothesis = int(profit_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if profit_hypothesis <= profit_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'profit_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the profit, any number of profit greater than 'profit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
