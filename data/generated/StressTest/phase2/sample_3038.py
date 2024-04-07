# Premise: In a friendship gang Aravind has 2 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Aravind has 7 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: contradiction

gangs_premise = 2
gangs_hypothesis = 7

# the hypothesis refers to the number of gangs in the premise
if gangs_hypothesis != gangs_premise:
    # check if the number of gangs in the hypothesis contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the number of gangs in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)

