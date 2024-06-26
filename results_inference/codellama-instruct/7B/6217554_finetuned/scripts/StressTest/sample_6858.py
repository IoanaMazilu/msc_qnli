walking_distance_premise = 4
walking_distance_hypothesis = 3

# the hypothesis refers to the walking distance mentioned in the premise
if walking_distance_hypothesis >= walking_distance_premise:
    # check if the estimate of 'walking_distance_hypothesis' contradicts the walking distance in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
