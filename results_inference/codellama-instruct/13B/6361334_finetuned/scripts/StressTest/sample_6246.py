investment_amount_premise = 100000
investment_amount_hypothesis = 600000
interest_rate_premise = 10
interest_rate_hypothesis = 10
period_premise = 3
period_hypothesis = 3

# the hypothesis refers to the investment amount and interest rate mentioned in the premise
if investment_amount_hypothesis >= investment_amount_premise:
    # check if the estimate of 'investment_amount_hypothesis' contradicts the investment amount in the premise
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
elif period_hypothesis!= period_premise:
    # check if the period in the hypothesis contradicts the period reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
