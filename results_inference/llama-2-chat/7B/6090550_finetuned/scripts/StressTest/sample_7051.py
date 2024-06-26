deepak_share_premise = 4300
deepak_share_hypothesis = 1300

# the hypothesis talks about the share of Deepak, referenced also in the premise
if deepak_share_hypothesis >= deepak_share_premise:
    # check if the hypothesis value contradicts the estimate of less than 'deepak_share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Deepak's share
    # any share less than 'deepak_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
