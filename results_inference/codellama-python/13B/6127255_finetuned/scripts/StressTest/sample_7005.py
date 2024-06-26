pets_premise = 96
pets_hypothesis = 56

# the hypothesis refers to the total number of pets (gerbils and hamsters) that Claire has, which is also mentioned in the premise
if pets_premise <= pets_hypothesis:
    # check if the number of pets in the premise contradicts the estimate of more than 'pets_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
