amount_premise = 3600
amount_hypothesis = 1600

# the hypothesis refers to the amount from Anwar mentioned in the premise
if amount_premise <= amount_hypothesis:
    # check if the estimate of 'amount_hypothesis' contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
