share_premise = 4500
share_hypothesis = 7500

# the hypothesis refers to the share of Tony, which is also mentioned in the premise
if share_hypothesis <= share_premise:
    # check if the hypothesis value contradicts the estimate of'share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the share of Tony
    # any number greater than'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
