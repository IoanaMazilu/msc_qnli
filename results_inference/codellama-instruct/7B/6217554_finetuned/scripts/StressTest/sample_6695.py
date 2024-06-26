withdrawal_amount_premise = 14000
withdrawal_amount_hypothesis = 14000

# the hypothesis refers to the amount of withdrawal mentioned in the premise
if withdrawal_amount_hypothesis >= withdrawal_amount_premise:
    # check if the hypothesis value contradicts the amount of withdrawal in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
