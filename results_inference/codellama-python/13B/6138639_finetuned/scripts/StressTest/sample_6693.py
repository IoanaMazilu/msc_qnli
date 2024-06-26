withdrawal_premise = 14000
withdrawal_hypothesis = 44000

# the hypothesis refers to the amount John withdraws after 8 months, mentioned in the premise
if withdrawal_premise >= withdrawal_hypothesis:
    # check if the estimate of 'withdrawal_hypothesis' contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
