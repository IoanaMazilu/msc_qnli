train_leaves_chennai_premise = 12
train_leaves_chennai_hypothesis = 82

if train_leaves_chennai_hypothesis <= train_leaves_chennai_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
