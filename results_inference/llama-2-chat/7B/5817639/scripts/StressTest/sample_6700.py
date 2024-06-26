share_premise = 6500
share_hypothesis = 4500

# the hypothesis talks about the share of Tony, referenced also in the premise
if share_hypothesis <= share_premise:
    # check if the hypothesis value contradicts the estimate of less than'share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the share,
    # any share greater than'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)