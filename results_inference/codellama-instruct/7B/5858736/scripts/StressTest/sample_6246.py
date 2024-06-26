# Define variables with representative names for the numerical entities in both inputs
investment_premise = 100000
interest_rate_premise = 10
period_premise = 3
investment_hypothesis = 600000

# Extract all quantities as valid numbers
investment_premise = float(investment_premise)
interest_rate_premise = float(interest_rate_premise)
period_premise = float(period_premise)
investment_hypothesis = float(investment_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if investment_hypothesis <= investment_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'investment_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the investment amount
    # Any amount greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
