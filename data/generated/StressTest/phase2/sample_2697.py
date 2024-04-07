# Premise: In a friendship gang Andrew has 8 gang, in how many ways can he invite one ormore of the gang to his house?
# Hypothesis: In a friendship gang Andrew has more than 1 gang, in how many ways can he invite one ormore of the gang to his house?
# Golden Label: entailment

gangs_premise = 8
gangs_hypothesis = 1

# the hypothesis refers to the number of gangs Andrew has, mentioned in the premise
if gangs_premise <= gangs_hypothesis:
    # check if the number of gangs in the hypothesis contradicts the number of gangs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
