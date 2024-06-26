train_distance_premise = 7
train_distance_hypothesis = 6

if train_distance_hypothesis <= train_distance_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
