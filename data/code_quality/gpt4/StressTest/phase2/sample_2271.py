ratio_premise = 2/3
ratio_hypothesis = 4/3

# the hypothesis talks about the ratio of distances between A to B and B to C, referenced also in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # the premise gives only a specific ratio for the distances
    # any ratio less than 'ratio_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
