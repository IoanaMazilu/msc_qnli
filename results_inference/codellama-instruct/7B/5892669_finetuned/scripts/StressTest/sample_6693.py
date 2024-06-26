withdraw_premise = 14000
withdraw_hypothesis = 44000

# the hypothesis refers to the amount John withdraws, mentioned in the premise
if withdraw_hypothesis <= withdraw_premise:
    # check if the estimate of 'withdraw_hypothesis' contradicts the amount John withdraws in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
