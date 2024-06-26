ratio_distance_premise = 2/3
ratio_distance_hypothesis = 8/3

# the hypothesis talks about the ratio of distances between A to B and B to C, referenced also in the premise
if ratio_distance_hypothesis!= ratio_distance_premise:
    # check if the ratio of distances in the hypothesis contradicts the ratio of distances reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
