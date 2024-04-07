# Premise: In a friendship gang Kala has 11 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Kala has less than 41 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: entailment

gang_members_premise = 11
gang_members_hypothesis = 41

# the hypothesis refers to the number of gang members mentioned in the premise
if gang_members_premise >= gang_members_hypothesis:
    # check if the estimate of 'gang_members_hypothesis' contradicts the number of gang members in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

