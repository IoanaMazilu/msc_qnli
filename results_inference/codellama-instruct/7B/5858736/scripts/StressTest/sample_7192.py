train_leaves_chennai_premise = 82
train_leaves_chennai_hypothesis = 12

if train_leaves_chennai_hypothesis <= train_leaves_chennai_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
