ratio_premise = 3/3
ratio_hypothesis = 1/3

# the hypothesis talks about the ratio of distances from A to B and B to C, which is also mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the ratio_hypothesis contradicts the ratio_premise
    label = "contradiction"
elif ratio_hypothesis < ratio_premise:
    # the premise gives the exact ratio of distances
    # any ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
