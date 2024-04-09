profit_premise = 6970
share_hypothesis = 1970

# the hypothesis talks about the share of Sameer in the profit, referenced also in the premise
if share_hypothesis <= profit_premise:
    # check if the hypothesis value contradicts the estimate of the share of Sameer in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the share of Sameer, any share greater than'share_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
