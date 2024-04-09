share_premise = 500
share_hypothesis = 600

# the hypothesis talks about the amount of money that Greg's share is worth, referenced also in the premise
if share_hypothesis <= share_premise:
    # check if the hypothesis value contradicts the estimate of more than'share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money that Greg's share is worth
    # any amount of money greater than'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
