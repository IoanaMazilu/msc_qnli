running_distance_premise = 2
running_distance_hypothesis = 3

# the hypothesis refers to the running distance of two sisters mentioned in the premise
if running_distance_premise != running_distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
