watermelons_premise = 136
watermelons_hypothesis = 136

# the hypothesis refers to the number of watermelons mentioned in the premise
if watermelons_premise <= watermelons_hypothesis:
    # check if the estimate of 'watermelons_hypothesis' contradicts the number of watermelons in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
