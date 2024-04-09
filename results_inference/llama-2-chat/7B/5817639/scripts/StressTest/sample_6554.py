members_premise = 30
members_hypothesis = 32

# the hypothesis talks about the number of members of a certain club traveling to different countries, referenced also in the premise
if members_hypothesis <= members_premise:
    # check if the hypothesis value contradicts the estimate of more than'members_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members traveling to each country
    # any number of members traveling to more than'members_premise' countries is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
