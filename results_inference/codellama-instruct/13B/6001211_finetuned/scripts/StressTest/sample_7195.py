train_time_premise = 6 + 1 / 24 # converting days to hours
train_time_hypothesis = 7 + 1 / 24 # converting days to hours

# the hypothesis refers to the time required by a train to cover the distance between Chennai and Jammu mentioned in the premise
if train_time_hypothesis <= train_time_premise:
    # check if the 'train_time_hypothesis' contradicts the time required by a train in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time required by a train
    # any time greater than 'train_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
