train_time_premise = 6 + 1/24/60  # 6 days and 1 minute converted to days
train_time_hypothesis = 7 + 1/24/60  # 7 days and 1 minute converted to days

# the hypothesis refers to the time required by a train to cover the distance between Chennai and Jammu, also mentioned in the premise
if train_time_hypothesis <= train_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'train_time_premise' days
    label = "contradiction"
else:
    # the premise gives only an estimate for the time required by the train
    # any time greater than 'train_time_premise' days is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
