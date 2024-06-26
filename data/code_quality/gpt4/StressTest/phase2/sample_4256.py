investment_amount_premise = 1000000000
investment_amount_hypothesis = 2000000000
interest_rate_premise = 10
interest_rate_hypothesis = 10
investment_period_premise = 3
investment_period_hypothesis = 3

# the hypothesis refers to the investment amount, interest rate and period mentioned in the premise
if investment_amount_premise != investment_amount_hypothesis:
    # check if the investment amount in the hypothesis contradicts the investment amount reported in the premise
    label = "contradiction"
elif interest_rate_premise != interest_rate_hypothesis:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
elif investment_period_premise != investment_period_hypothesis:
    # check if the investment period in the hypothesis contradicts the investment period reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
