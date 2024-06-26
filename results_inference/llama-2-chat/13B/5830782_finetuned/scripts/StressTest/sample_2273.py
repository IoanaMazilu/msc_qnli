ratio_distances_premise = [2, 3]
ratio_distances_hypothesis = [8, 3]

# the hypothesis refers to the same scenario as the premise, but changes the ratio of distances
if ratio_distances_hypothesis!= ratio_distances_premise:
    # check if the ratio of distances in the hypothesis contradicts the ratio of distances in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
