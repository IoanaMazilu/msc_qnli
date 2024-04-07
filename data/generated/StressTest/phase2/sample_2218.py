# Premise: In a friendship gang Andrew has more than 1 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Andrew has 8 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: neutral

gangs_premise = 1
gangs_hypothesis = 8

# the hypothesis provides a specific number of gangs Andrew has, which is also referenced in the premise
if gangs_hypothesis <= gangs_premise:
    # check if the number of gangs in the hypothesis contradicts the premise estimate of more than 'gangs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gangs
    # any number of gangs greater than 'gangs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

