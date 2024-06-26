deepak_share_premise = 1300
deepak_share_hypothesis = 4300

if deepak_share_hypothesis <= deepak_share_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Deepak's share
    # any number of shares greater than 'deepak_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
