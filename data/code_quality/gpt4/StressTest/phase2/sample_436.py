share_deepak_premise = 2380
share_deepak_hypothesis = 1380

# the hypothesis refers to Deepak's share mentioned in the premise
if share_deepak_hypothesis >= share_deepak_premise:
    # check if the value of 'share_deepak_hypothesis' contradicts the premise of less than 'share_deepak_premise'
    label = "contradiction"
elif share_deepak_hypothesis < share_deepak_premise:
    # the hypothesis value is less than 'share_deepak_premise', which is consistent with the premise
    # but the exact amount cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
