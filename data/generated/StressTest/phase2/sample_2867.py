# Premise: In a friendship gang Kala has 11 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Kala has 71 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: contradiction

gang_premise = 11
gang_hypothesis = 71

# the hypothesis refers to the number of gangs Kala has, which is also mentioned in the premise
if gang_premise != gang_hypothesis:
    # check if the number of gangs in the hypothesis contradicts the number of gangs mentioned in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are the same
    label = "entailment"

print(label)

