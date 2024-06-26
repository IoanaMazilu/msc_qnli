share_diff_premise = 300
share_diff_hypothesis = 800

# the hypothesis refers to the difference between Raja and Rahim's share mentioned in the premise
if share_diff_hypothesis <= share_diff_premise:
    # check if the estimate of 'share_diff_hypothesis' contradicts the share difference in the premise
    label = "contradiction"
elif share_diff_hypothesis > share_diff_premise:
    # since the premise does not specify an upper limit for the share difference, any value greater than 'share_diff_premise' is consistent with it, but not explicitly entailed
    label = "neutral"

print(label)
