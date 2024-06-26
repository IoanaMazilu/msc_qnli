members_premise = 59
members_hypothesis = 19

# the hypothesis talks about the number of members in a class, referenced also in the premise
if members_hypothesis <= members_premise:
    # check if the hypothesis value contradicts the estimate of'members_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members
    # any number of members greater than'members_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
