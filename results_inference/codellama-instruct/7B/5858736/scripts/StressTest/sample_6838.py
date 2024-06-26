# Define variables with representative names for the numerical entities in both inputs
total_earnings_premise = 4000
total_earnings_hypothesis = 9000

# Extract all quantities as valid numbers (integers or floats)
total_earnings_premise = int(total_earnings_premise)
total_earnings_hypothesis = int(total_earnings_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if total_earnings_hypothesis <= total_earnings_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'total_earnings_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the total earnings, any number greater than 'total_earnings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
