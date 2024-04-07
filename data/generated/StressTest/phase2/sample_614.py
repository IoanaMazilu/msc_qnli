# Premise: In a friendship gang Andrew has 8 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Andrew has 4 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: contradiction

gang_count_premise = 8
gang_count_hypothesis = 4

# the hypothesis refers to the number of gangs Andrew has, also mentioned in the premise
if gang_count_hypothesis != gang_count_premise:
    # check if the number of gangs in the hypothesis contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the number of gangs in the hypothesis does not contradict the number of gangs in the premise, we can infer entailment
    label = "entailment"

print(label)

