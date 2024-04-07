# Premise: In a friendship gang Angel has less than 7 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Angel has 3 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: neutral

gang_members_premise = 7
gang_members_hypothesis = 3

# the hypothesis provides a specific number for the gang members which is also mentioned in the premise
if gang_members_hypothesis >= gang_members_premise:
    # check if the number of gang members in the hypothesis contradicts the estimate of less than 'gang_members_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gang members
    # any number of gang members less than 'gang_members_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
