gang_members_premise = 5
gang_members_hypothesis = 5

# the hypothesis refers to the number of gang members mentioned in the premise
if gang_members_hypothesis <= gang_members_premise:
    # check if the hypothesis value contradicts the number of gang members in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gang members
    # any number of gang members greater than 'gang_members_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
