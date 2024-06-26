share_tony_premise = 4500
share_tony_hypothesis = 7500

# the hypothesis refers to the share of Tony mentioned in the premise
if share_tony_hypothesis == share_tony_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the share of Tony
    # any share greater than'share_tony_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
