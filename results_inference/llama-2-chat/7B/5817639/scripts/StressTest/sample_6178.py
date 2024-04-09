ratio_premise = 6/3
ratio_hypothesis = 4/3

# the hypothesis talks about the ratio between two people and their age after 6 years
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio and the hypothesis value is consistent with it, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
