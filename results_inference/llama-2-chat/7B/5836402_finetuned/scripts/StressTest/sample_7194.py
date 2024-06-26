train_distance_premise = 7 * 24 + 1
train_distance_hypothesis = 6 * 24 + 1

# the hypothesis refers to the distance covered by the train mentioned in the premise
if train_distance_hypothesis <= train_distance_premise:
    # check if the estimate of 'train_distance_hypothesis' contradicts the exact distance in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
