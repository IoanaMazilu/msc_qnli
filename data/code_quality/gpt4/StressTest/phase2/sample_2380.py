ratio_premise = 4 / 3
ratio_hypothesis = 2 / 3

# the hypothesis and premise are discussing the ratio of distances between points A to B and B to C
if ratio_hypothesis >= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif ratio_hypothesis == ratio_premise:
    # if the ratio values in the hypothesis and premise are equal, it's entailment
    label = "entailment"
else:
    # the premise gives an estimate for the ratio of distances
    # a ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
