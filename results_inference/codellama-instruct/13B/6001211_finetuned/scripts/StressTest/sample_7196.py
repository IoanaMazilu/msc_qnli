train_time_premise = 7 * 24 * 60 + 1  # converting days to minutes
train_time_hypothesis = 7 * 24 * 60 + 1  # converting days to minutes

# the hypothesis refers to the time required by a train to cover the distance between Chennai and Jammu mentioned in the premise
if train_time_hypothesis <= train_time_premise:
    # check if the hypothesis value contradicts the exact time mentioned in the premise
    label = "contradiction"
else:
    # the premise gives the exact time required by a train to cover the distance between Chennai and Jammu
    # any time greater than 'train_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
