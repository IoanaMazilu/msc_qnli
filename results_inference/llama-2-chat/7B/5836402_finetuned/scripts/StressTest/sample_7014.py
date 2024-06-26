lewis_brown_ratio_premise = 1/2
lewis_brown_ratio_hypothesis = 6/2

# the hypothesis talks about the ratio of the present ages of Lewis and Brown, referenced also in the premise
if lewis_brown_ratio_hypothesis > lewis_brown_ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimate of less than 'lewis_brown_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio less than 'lewis_brown_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
