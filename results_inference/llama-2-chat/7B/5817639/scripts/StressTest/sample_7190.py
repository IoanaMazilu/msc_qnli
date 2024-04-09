train_leaves_jammu_premise = "12 noon"
train_leaves_jammu_hypothesis = "62 noon"

# the hypothesis refers to the time at which a train leaves Jammu, which is also mentioned in the premise
if train_leaves_jammu_premise <= train_leaves_jammu_hypothesis:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of departure,
    # any time different from 'train_leaves_jammu_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
