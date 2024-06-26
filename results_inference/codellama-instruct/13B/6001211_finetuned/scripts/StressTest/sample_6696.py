withdraw_premise = 2000
withdraw_hypothesis = 5000

# the hypothesis refers to the amount Tony withdraws, which is also mentioned in the premise
if withdraw_hypothesis <= withdraw_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif withdraw_premise >= withdraw_hypothesis:
    # check if the premise value contradicts the hypothesis value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
