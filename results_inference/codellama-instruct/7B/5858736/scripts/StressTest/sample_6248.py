# Define variables with representative names for the numerical entities in both inputs
investment_premise = 100000
interest_rate_premise = 10
period_premise = 3
investment_hypothesis = 100000
interest_rate_hypothesis = 10
period_hypothesis = 3

# Extract all quantities as valid numbers (integers or floats)
investment_premise = float(investment_premise)
interest_rate_premise = float(interest_rate_premise)
period_premise = float(period_premise)
investment_hypothesis = float(investment_hypothesis)
interest_rate_hypothesis = float(interest_rate_hypothesis)
period_hypothesis = float(period_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if investment_hypothesis <= investment_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'investment_premise'
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # Check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
elif period_hypothesis!= period_premise:
    # Check if the period in the hypothesis contradicts the period reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
