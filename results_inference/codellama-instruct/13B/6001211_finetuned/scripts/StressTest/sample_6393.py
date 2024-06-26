oil_premise = 8
oil_hypothesis = 7

# the hypothesis refers to the amount of oil needed for each car cylinder mentioned in the premise
if oil_premise <= oil_hypothesis:
    # check if the estimate of 'oil_hypothesis' contradicts the amount of oil in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
