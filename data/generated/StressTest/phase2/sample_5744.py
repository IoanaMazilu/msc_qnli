# Premise: In a friendship gang Andrew has 8 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Andrew has 2 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: contradiction

gang_members_premise = 8
gang_members_hypothesis = 2

# the hypothesis talks about the number of gang members Andrew has, referenced also in the premise
if gang_members_hypothesis != gang_members_premise:
    # check if the number of gang members in the hypothesis contradicts the number of gang members mentioned in the premise
    label = "contradiction"
else:
    # if the number of gang members in the hypothesis is the same as the premise, then we can infer entailment
    label = "entailment"

print(label)

