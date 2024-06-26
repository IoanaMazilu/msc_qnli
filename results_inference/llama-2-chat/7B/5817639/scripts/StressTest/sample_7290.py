share_premise = 600
share_hypothesis = 500

# the hypothesis talks about the amount of money Greg's share is, referenced also in the premise
if share_hypothesis <= share_premise:
    # check if the hypothesis value contradicts the estimate of'share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money Greg's share is
    # any amount of money greater than'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
