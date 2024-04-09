members_traveled_premise = 8
members_traveled_hypothesis = 6

# the hypothesis talks about the number of members who traveled to both England and France, referenced also in the premise
if members_traveled_hypothesis <= members_traveled_premise:
    # check if the hypothesis value contradicts the estimate of less than'members_traveled_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members who traveled to both England and France
    # any number of members who traveled to both England and France greater than'members_traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
