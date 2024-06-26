gang_premise = 8
gang_hypothesis = 3

# the hypothesis refers to the number of gangs Andrew has, which is also mentioned in the premise
if gang_premise <= gang_hypothesis:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
