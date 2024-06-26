ratio_premise = 3/4
ratio_hypothesis = 5/4

if ratio_hypothesis <= ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimate of more than 'ratio_premise' in the premise
    label = "contradiction"
else:
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
