share_premise = 1300
share_hypothesis = 4300

# the hypothesis talks about the share of a person, referenced also in the premise
if share_hypothesis <= share_premise:
    # check if the hypothesis value contradicts the estimate of Deepak's share in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Deepak's share
    # any share value greater than'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
