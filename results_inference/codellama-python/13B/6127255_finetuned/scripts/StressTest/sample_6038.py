members_premise = 59
members_hypothesis = 59

# the hypothesis refers to the number of members in the school class mentioned in the premise
if members_hypothesis <= members_premise:
    # check if the estimate of'members_hypothesis' contradicts the number of members in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of members
    # any number of members greater than'members_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
