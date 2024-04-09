oil_requirement_premise = 8
oil_requirement_hypothesis = 7

# the hypothesis refers to the amount of oil required for each cylinder mentioned in the premise
if oil_requirement_premise <= oil_requirement_hypothesis:
    # check if the 'oil_requirement_hypothesis' contradicts the amount of oil required in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
