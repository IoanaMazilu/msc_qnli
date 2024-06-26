share_premise = 500
share_hypothesis = 600

# the hypothesis talks about the share of Greg, referenced also in the premise
if share_hypothesis <= share_premise:
    # check if the hypothesis value contradicts the estimate of more than'share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the share
    # any share greater than'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
