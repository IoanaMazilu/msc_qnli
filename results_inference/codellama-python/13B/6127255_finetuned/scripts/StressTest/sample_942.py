gang_premise = 8
gang_hypothesis = 3

# the hypothesis refers to the number of gangs Andrew has, mentioned in the premise
if gang_premise <= gang_hypothesis:
    # check if the estimate of 'gang_hypothesis' contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)