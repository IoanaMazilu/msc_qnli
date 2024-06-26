investment_amount_premise = 100000
investment_amount_hypothesis = 100000
interest_rate_premise = 10
interest_rate_hypothesis = 10
period_premise = 3
period_hypothesis = 3

# the hypothesis refers to the same investment scenario as the premise
if investment_amount_hypothesis >= investment_amount_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise or period_hypothesis!= period_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
