gangs_premise = 5
gangs_hypothesis = 2

# the hypothesis refers to the number of gangs Mala has, also mentioned in the premise
if gangs_premise <= gangs_hypothesis:
    # check if the number of gangs in the premise is less than or equal to the number of gangs in the hypothesis
    label = "contradiction"
else:
    # if the number of gangs in the premise is greater than the number of gangs in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
