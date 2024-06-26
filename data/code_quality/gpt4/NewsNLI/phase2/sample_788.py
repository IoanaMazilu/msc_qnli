amount_premise = 958000
amount_hypothesis = 958000

# the hypothesis mentions the amount of money raised, which is also referenced in the premise
if amount_hypothesis != amount_premise:
    # check if the amount of money raised in the hypothesis contradicts the amount stated in the premise
    label = "contradiction"
else:
    # if the amount of money raised in the hypothesis does not contradict the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
