# Premise: In a friendship gang Andrew has 8 gang, in how many ways can he invite one ormore of the gang to his house?
# Hypothesis: In a friendship gang Andrew has more than 8 gang, in how many ways can he invite one ormore of the gang to his house?
# Golden Label: contradiction

gang_premise = 8
gang_hypothesis = 8

# the hypothesis talks about the number of gangs Andrew has, referenced also in the premise
if gang_hypothesis > gang_premise:
    # check if the hypothesis value contradicts the exact number of 'gang_premise'
    label = "contradiction"
elif gang_hypothesis == gang_premise:
    # if the hypothesis value is equal to the premise ones, we can infer entailment
    label = "entailment"
else:
    # the premise gives exact number for the gangs
    # any number of gangs less than 'gang_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

