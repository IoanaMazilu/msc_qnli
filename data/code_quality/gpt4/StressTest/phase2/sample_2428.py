old_ratio_premise = 7/3
old_ratio_hypothesis = 5/3

# the hypothesis refers to the ratio of ages of two people in the future, referenced also in the premise
if old_ratio_hypothesis >= old_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'old_ratio_premise'
    label = "contradiction"
else:
    # any ratio of ages less than 'old_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
