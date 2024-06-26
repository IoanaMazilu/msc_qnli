ratio_distances_premise = [4, 2]
ratio_distances_hypothesis = [3, 2]

# the hypothesis refers to the ratio of distances between A to B and B to C mentioned in the premise
if ratio_distances_premise!= ratio_distances_hypothesis:
    # check if the ratio of distances in the hypothesis contradicts the ratio of distances reported in the premise
    label = "contradiction"
else:
    # if the ratio of distances in the hypothesis does not contradict the ratio of distances in the premise, we can infer entailment
    label = "entailment"

print(label)
