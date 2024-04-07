# Premise: In a friendship gang Andrew has 8 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Andrew has less than 8 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: contradiction

gang_members_premise = 8
gang_members_hypothesis = 8

# the hypothesis refers to the number of gang members mentioned in the premise
if gang_members_hypothesis >= gang_members_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

