investment_premise = 100000000
investment_hypothesis = 100000000
interest_rate_premise = 10
interest_rate_hypothesis = 10
period_premise = 3
period_hypothesis = 3

# the hypothesis refers to the investment, interest rate, and period mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the value in the hypothesis contradicts the investment in the premise
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise or period_hypothesis != period_premise:
    # check if the interest rate or period in the hypothesis contradicts the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
