ratio_premise = 6
ratio_hypothesis = 1

# the hypothesis talks about the ratio of the ages of Lewis and Brown, which is also mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio,
    # any ratio greater than the ratio in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
