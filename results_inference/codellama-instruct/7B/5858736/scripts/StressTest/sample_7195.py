train_distance_premise = 6.01
train_distance_hypothesis = 7.01

if train_distance_hypothesis <= train_distance_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
