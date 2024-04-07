# Premise: In a friendship gang Andrew has 8 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Andrew has 5 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: contradiction

gang_premise = 8
gang_hypothesis = 5

# The hypothesis refers to the number of gangs Andrew has, mentioned also in the premise
if gang_hypothesis != gang_premise:
    # if the number of gangs in the hypothesis contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # The premise and hypothesis are same
    label = "entailment"

print(label)

