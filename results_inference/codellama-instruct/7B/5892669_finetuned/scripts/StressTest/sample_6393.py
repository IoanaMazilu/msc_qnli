oil_premise = 8
oil_hypothesis = 7

# the hypothesis refers to the amount of oil used in George's car, mentioned in the premise
if oil_premise <= oil_hypothesis:
    # check if the estimate of 'oil_hypothesis' contradicts the amount of oil used in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
