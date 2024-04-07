# Premise: The present ages of Lewis and Brown are in the ratio less than 6:2.
# Hypothesis: The present ages of Lewis and Brown are in the ratio 1:2.
# Golden Label: neutral

lewis_brown_ratio_premise = 6 / 2
lewis_brown_ratio_hypothesis = 1 / 2

# the hypothesis talks about the ratio of the ages of Lewis and Brown, referenced also in the premise
if lewis_brown_ratio_hypothesis >= lewis_brown_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'lewis_brown_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the ages
    # any ratio less than 'lewis_brown_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

