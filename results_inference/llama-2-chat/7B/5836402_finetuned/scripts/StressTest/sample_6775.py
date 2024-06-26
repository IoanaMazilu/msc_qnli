ratio_distances_premise = 1
ratio_distances_hypothesis = 4

# the hypothesis refers to the ratio of distances between A to B and B to C, which is also mentioned in the premise
if ratio_distances_hypothesis < ratio_distances_premise:
    # check if the ratio of distances in the hypothesis contradicts the estimate of more than 'ratio_distances_premise'
    label = "contradiction"
elif ratio_distances_hypothesis > ratio_distances_premise:
    # check if the ratio of distances in the hypothesis is greater than the estimate in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
