ratio_premise = 7/3
ratio_hypothesis = 1/3

# the hypothesis refers to the ratio of the ages of Anil and his son
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
