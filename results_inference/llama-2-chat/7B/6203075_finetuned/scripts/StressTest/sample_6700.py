share_tony_premise = 6500
share_tony_hypothesis = 4500

# the hypothesis refers to the share of Tony mentioned in the premise
if share_tony_hypothesis >= share_tony_premise:
    # check if the hypothesis value contradicts the estimate of less than'share_tony_premise'
    label = "contradiction"
elif share_tony_hypothesis < share_tony_premise:
    # the premise gives an estimate for the share of Tony
    # any share less than'share_tony_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
