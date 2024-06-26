amount_premise = 3600
amount_hypothesis = 3600
interest_premise = 0.06
interest_hypothesis = 0.06

# the hypothesis refers to the amount and interest rate mentioned in the premise
if amount_hypothesis > amount_premise:
    # check if the amount in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
elif interest_hypothesis != interest_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
