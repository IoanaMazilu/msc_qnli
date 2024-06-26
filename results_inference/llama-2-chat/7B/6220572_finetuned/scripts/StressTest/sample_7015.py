lewis_brown_ratio_premise = 6/2
lewis_brown_ratio_hypothesis = 1/2

# the hypothesis refers to the ratio of the ages of Lewis and Brown mentioned in the premise
if lewis_brown_ratio_hypothesis!= lewis_brown_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages
    # any ratio less than 'lewis_brown_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
