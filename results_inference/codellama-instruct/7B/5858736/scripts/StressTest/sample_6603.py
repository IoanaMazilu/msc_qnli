# Define variables with representative names for the numerical entities in both inputs
original_investment = 200
years = 5

# Extract all quantities as valid numbers (integers or floats)
investment_at_end = 200 * 2

# Use brief comments to explain what comparison you do between the defined variables
if investment_at_end < 3 * original_investment:
    # Check if the estimate of 'investment_at_end' contradicts the number of investment reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
