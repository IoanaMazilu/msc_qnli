train_time_premise = 82
train_time_hypothesis = 12

# the hypothesis refers to the time of the train departure mentioned in the premise
if train_time_hypothesis > train_time_premise:
    # check if the hypothesis time contradicts the estimate of less than 'train_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the train time
    # any time less than 'train_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
