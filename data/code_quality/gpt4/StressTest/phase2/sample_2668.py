train_time_premise = 3
train_time_hypothesis = 9

# the hypothesis mentions a specific time when a train leaves Delhi, also referenced in the premise
if train_time_hypothesis <= train_time_premise:
    # check if the hypothesis time contradicts the premise which states that the train leaves after 'train_time_premise'
    label = "contradiction"
else:
    # the premise gives only a lower limit for the train departure time
    # any departure time greater than 'train_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
