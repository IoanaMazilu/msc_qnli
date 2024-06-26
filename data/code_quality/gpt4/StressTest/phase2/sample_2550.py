dist_ratio_premise = 2/3
dist_ratio_hypothesis = 1

# the hypothesis refers to the ratio of distances between A to B and B to C, also mentioned in the premise
if dist_ratio_hypothesis > dist_ratio_premise:
    # check if the hypothesis value contradicts the ratio of the distances in the premise
    label = "contradiction"
elif dist_ratio_hypothesis != dist_ratio_premise:
    # check if the ratio in the hypothesis is different from the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
