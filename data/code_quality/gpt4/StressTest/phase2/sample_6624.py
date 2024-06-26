ratio_sheep_horses_premise = 6 / 7
ratio_sheep_horses_hypothesis = 1 / 7

# The hypothesis refers to the ratio of sheep to horses mentioned in the premise.
if ratio_sheep_horses_hypothesis >= ratio_sheep_horses_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise.
    label = "contradiction"
else:
    # the hypothesis value does not contradict the premise value but it cannot be explicitly entailed from the premise.
    label = "neutral"

print(label)
