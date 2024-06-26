invested_amount_premise = 100000
invested_amount_hypothesis = 600000
interest_rate_premise = 10
interest_rate_hypothesis = 10
period_premise = 3
period_hypothesis = 3

# the hypothesis refers to the same period and interest rate as the premise
if invested_amount_hypothesis <= invested_amount_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise or period_hypothesis!= period_premise:
    # check if the interest rate or period in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
