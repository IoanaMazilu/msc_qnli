ratio_premise = 1
ratio_hypothesis = 0.5

# the hypothesis talks about a ratio of ages, which is also referred to in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio of ages, and the hypothesis value cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
