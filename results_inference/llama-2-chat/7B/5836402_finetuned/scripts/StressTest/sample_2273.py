distance_ratio_premise = 2/3
distance_ratio_hypothesis = 8/3

# the hypothesis refers to the ratio of distances between A to B and B to C, which is also mentioned in the premise
if distance_ratio_hypothesis!= distance_ratio_premise:
    # check if the ratio of distances in the hypothesis contradicts the ratio of distances reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
