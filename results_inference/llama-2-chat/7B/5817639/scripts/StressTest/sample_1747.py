ratio_premise = 1
ratio_hypothesis = 5

# the hypothesis talks about the ratio of ages, which is also referred to in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio, any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
