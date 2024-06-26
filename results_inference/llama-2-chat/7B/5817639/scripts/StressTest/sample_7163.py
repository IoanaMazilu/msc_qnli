ratio_premise = 4/3/1
ratio_hypothesis = 3/4/1

# the hypothesis refers to a different ratio than the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio, and any ratio less than 4:3:1 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
