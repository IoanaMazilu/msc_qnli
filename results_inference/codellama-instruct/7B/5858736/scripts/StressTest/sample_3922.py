train_leaves_delhi_premise = 4
train_leaves_delhi_hypothesis = 9

if train_leaves_delhi_hypothesis <= train_leaves_delhi_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
