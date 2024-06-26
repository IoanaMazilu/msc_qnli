gang_premise = 5
gang_hypothesis = 2

# the hypothesis refers to the number of gangs Mala has, mentioned in the premise
if gang_premise <= gang_hypothesis:
    # check if the estimate of 'gang_hypothesis' contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
