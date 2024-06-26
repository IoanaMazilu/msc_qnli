train_leave_time_premise = 82
train_leave_time_hypothesis = 12

# the hypothesis talks about the time a train leaves, which is also referenced in the premise
if train_leave_time_hypothesis >= train_leave_time_premise:
    # check if the hypothesis time contradicts the premise of the train leaving before 'train_leave_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time the train leaves
    # any time before 'train_leave_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
