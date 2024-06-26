running_distance_premise = 12
running_distance_hypothesis = 52

# the hypothesis refers to the distance the twins sisters ran in opposite directions, mentioned in the premise
if running_distance_premise >= running_distance_hypothesis:
    # check if the estimate of 'running_distance_hypothesis' contradicts the distance the twins sisters ran in opposite directions mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
