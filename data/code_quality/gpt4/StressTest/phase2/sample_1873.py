investment_premise = 80000000
investment_hypothesis = 10000000
interest_rate_premise = 10
interest_rate_hypothesis = 10
period_premise = 3
period_hypothesis = 3

# the hypothesis refers to the amount of investment, the interest rate and the period mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the amount of 'investment_hypothesis' contradicts the estimate of less than 'investment_premise'
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise or period_hypothesis != period_premise:
    # check if the interest rate or the period in the hypothesis contradict the same values reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
