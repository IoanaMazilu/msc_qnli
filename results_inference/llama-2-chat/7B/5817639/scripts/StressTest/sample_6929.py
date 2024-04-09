age_ratio_premise = 4
age_ratio_hypothesis = 5

# the hypothesis talks about the ratio between the ages of Sandy and Molly, which is also referred to in the premise
if age_ratio_premise <= age_ratio_hypothesis:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio, and any ratio greater than 4:3 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
