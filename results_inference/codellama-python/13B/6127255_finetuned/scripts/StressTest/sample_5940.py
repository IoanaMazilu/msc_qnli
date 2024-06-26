gang_premise = 5
gang_hypothesis = 2

# the hypothesis refers to the number of gangs Mala has, which is also mentioned in the premise
if gang_premise <= gang_hypothesis:
    # check if the number of gangs in the hypothesis contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the number of gangs in the hypothesis does not contradict the number of gangs in the premise, we can infer entailment
    label = "entailment"

print(label)
