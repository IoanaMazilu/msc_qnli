train_leaves_premise = 12
train_leaves_hypothesis = 82

# the hypothesis refers to the time at which the train leaves Chennai, mentioned in the premise
if train_leaves_hypothesis >= train_leaves_premise:
    # check if the hypothesis value contradicts the premise value of exactly 'train_leaves_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
