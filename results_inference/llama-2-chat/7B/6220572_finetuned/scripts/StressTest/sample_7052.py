share_premise = 1300
share_hypothesis = 1300

# the hypothesis talks about the share of Deepak, referenced also in the premise
if share_hypothesis >= share_premise:
    # check if the hypothesis value contradicts the estimate of less than'share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the share of Deepak
    # any share less than'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
