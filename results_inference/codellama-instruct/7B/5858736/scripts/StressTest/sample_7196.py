train_distance_premise = 7
train_distance_hypothesis = 7
train_time_premise = 1
train_time_hypothesis = 1

# the hypothesis refers to the time required by the train to cover the distance between Chennai and Jammu
if train_time_hypothesis <= train_time_premise:
    # check if the estimate of 'train_time_hypothesis' contradicts the time required by the train to cover the distance between Chennai and Jammu
    label = "contradiction"
else:
    # the premise gives only an estimate for the time required by the train to cover the distance between Chennai and Jammu
    # any time greater than 'train_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
