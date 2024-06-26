train_leaves_delhi_premise = 9
train_leaves_delhi_hypothesis = 4

if train_leaves_delhi_hypothesis <= train_leaves_delhi_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
