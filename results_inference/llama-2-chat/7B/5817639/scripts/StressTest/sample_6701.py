share_premise = 4500
share_hypothesis = 7500

# the hypothesis talks about the share of Tony, which is also mentioned in the premise
if share_hypothesis >= share_premise:
    # check if the hypothesis value contradicts the estimate of the share in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the share,
    # any share greater than or equal to'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
