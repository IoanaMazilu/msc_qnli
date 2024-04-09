train_leaves_delhi_premise = 4
train_leaves_delhi_hypothesis = 9

# the hypothesis refers to the time at which a train leaves Delhi, mentioned in the premise
if train_leaves_delhi_hypothesis <= train_leaves_delhi_premise:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
else:
    # the premise gives only an estimate for the time, any time greater than 'train_leaves_delhi_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
