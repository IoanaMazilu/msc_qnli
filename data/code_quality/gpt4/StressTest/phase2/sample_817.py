ratio_premise = 3/5
ratio_hypothesis = 2/5

# The hypothesis talks about the ratio of distances from A to B and B to C, which is also referenced in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimate of less than 'ratio_premise'
    label = "contradiction"
elif ratio_hypothesis < ratio_premise:
    # the premise gives only an estimate for the ratio of distances
    # any ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
