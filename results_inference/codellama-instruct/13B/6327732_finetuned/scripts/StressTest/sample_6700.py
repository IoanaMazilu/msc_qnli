share_premise = 6500
share_hypothesis = 4500

# the hypothesis refers to the number of shares mentioned in the premise
if share_hypothesis >= share_premise:
    # check if the hypothesis value contradicts the estimate of less than'share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shares
    # any number of shares less than'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
