share_sameer_premise = 6970
share_sameer_hypothesis = 1970

# the hypothesis refers to the share of Sameer in the profit mentioned in the premise
if share_sameer_hypothesis <= share_sameer_premise:
    # check if the hypothesis value contradicts the estimate of more than'share_sameer_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the share of Sameer
    # any share greater than'share_sameer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
