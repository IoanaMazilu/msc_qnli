# Premise: less than 800, what will be the difference between Raja and Rahim's share?
# Hypothesis: 300, what will be the difference between Raja and Rahim's share?
# Golden Label: neutral

share_difference_premise = 800
share_difference_hypothesis = 300

# The hypothesis addresses the difference between Raja and Rahim's share, which is also mentioned in the premise
if share_difference_hypothesis >= share_difference_premise:
    # check if the hypothesis value contradicts the estimate of less than 'share_difference_premise'
    label = "contradiction"
elif share_difference_hypothesis < share_difference_premise:
    # the premise gives only an estimate for the share difference
    # any share difference less than 'share_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

