gang_mala_premise = 5
gang_mala_hypothesis = 2

# the hypothesis refers to the number of gangs Mala has, mentioned in the premise
if gang_mala_premise <= gang_mala_hypothesis:
    # check if the estimate of 'gang_mala_hypothesis' contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
