share_deepak_premise = 4300
share_deepak_hypothesis = 1300

# the hypothesis talks about the share of Deepak, which is also mentioned in the premise
if share_deepak_hypothesis >= share_deepak_premise:
    # check if the hypothesis value contradicts the estimate of less than'share_deepak_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the share of Deepak
    # any share less than'share_deepak_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
