share_premise = 4500
share_hypothesis = 6500

# the hypothesis talks about the number of shares, referenced also in the premise
if share_hypothesis >= share_premise:
    # check if the hypothesis value contradicts the estimate of less than'share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shares
    # any number of shares less than'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
