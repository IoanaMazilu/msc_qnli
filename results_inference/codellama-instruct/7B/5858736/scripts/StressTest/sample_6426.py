# Define variables with representative names for the numerical entities in both inputs
total_price_premise = 450
total_price_hypothesis = 750

# Extract all quantities as valid numbers (integers or floats)
total_price_premise = int(total_price_premise)
total_price_hypothesis = int(total_price_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if total_price_hypothesis <= total_price_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'total_price_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the total price
    # Any number of roses greater than 'total_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
