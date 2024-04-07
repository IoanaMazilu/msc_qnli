# Premise: In a friendship gang Raja has 9 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Raja has 5 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: contradiction

gang_members_premise = 9
gang_members_hypothesis = 5

# the hypothesis talks about the number of members in Raja's gang, which is also mentioned in the premise
if gang_members_hypothesis != gang_members_premise:
    # check if the number of gang members in the hypothesis contradicts the number of gang members mentioned in the premise
    label = "contradiction"
else:
    # if the number of gang members in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)

