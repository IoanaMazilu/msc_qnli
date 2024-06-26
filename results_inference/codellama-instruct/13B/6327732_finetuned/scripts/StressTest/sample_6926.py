gang_premise = 8
gang_hypothesis = 7

# the hypothesis refers to the number of gang members in a friendship gang
if gang_hypothesis >= gang_premise:
    # check if the hypothesis value contradicts the number of gang members in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of gang members
    # any number of ways to invite one or more gang members to Andrew's house is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
