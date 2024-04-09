train_departs_premise = 9
train_departs_hypothesis = 1

# the hypothesis refers to the time when the train leaves Delhi, which is also mentioned in the premise
if train_departs_premise == train_departs_hypothesis:
    # the hypothesis value is consistent with the premise value, no contradiction or entailment can be inferred
    label = "neutral"
else:
    # the hypothesis value is different from the premise value, we can infer contradiction
    label = "contradiction"

print(label)
