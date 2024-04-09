ratio_premise = 4/3
ratio_hypothesis = 3/3

# the hypothesis refers to a different ratio than the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
