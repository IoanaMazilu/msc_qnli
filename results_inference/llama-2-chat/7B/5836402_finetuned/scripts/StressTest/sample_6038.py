members_premise = 59
members_hypothesis = 59

# the hypothesis refers to the number of members in Lourdes school class, which is also mentioned in the premise
if members_hypothesis <= members_premise:
    # check if the hypothesis value contradicts the estimate of more than'members_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members
    # any number of members greater than'members_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
