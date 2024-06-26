withdraw_premise = 2000
withdraw_hypothesis = 7000

# the hypothesis refers to the amount Tony withdraws, which is also mentioned in the premise
if withdraw_hypothesis!= withdraw_premise:
    # check if the amount Tony withdraws in the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
