investment_premise = 8000
investment_hypothesis = 5000
years_premise = 2
years_hypothesis = 2
interest_rate_premise = 0.05  # 5% converted to a decimal
interest_rate_hypothesis = 0.05  # 5% converted to a decimal

# The hypothesis refers to the amount invested, the period of investment and the interest rate, all mentioned in the premise
if investment_premise < investment_hypothesis:
    # Check if the investment amount in the premise contradicts the hypothesis of more than 'investment_hypothesis'
    label = "contradiction"
elif years_premise != years_hypothesis or interest_rate_premise != interest_rate_hypothesis:
    # Check if the period of investment or the interest rate in the hypothesis contradicts the respective values in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
