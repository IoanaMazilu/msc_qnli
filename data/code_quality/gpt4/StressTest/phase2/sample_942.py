gangs_premise = 8
gangs_hypothesis = 3

# the hypothesis refers to the number of gangs mentioned in the premise
if gangs_premise <= gangs_hypothesis:
    # check if the 'gangs_hypothesis' contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
