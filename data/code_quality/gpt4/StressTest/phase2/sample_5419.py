share_premise = 550
share_hypothesis = 250

# the hypothesis refers to Andre's share mentioned in the premise
if share_hypothesis >= share_premise:
    # check if the value of 'share_hypothesis' contradicts the estimate of less than 'share_premise'
    label = "contradiction"
elif share_hypothesis <= share_premise:
    # the premise gives only an estimate for the share
    # any share less than 'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
