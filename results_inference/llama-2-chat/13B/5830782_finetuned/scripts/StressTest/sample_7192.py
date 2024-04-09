train_departure_premise = 82
train_departure_hypothesis = 12

# the hypothesis talks about the train departure time, referenced also in the premise
if train_departure_hypothesis >= train_departure_premise:
    # check if the hypothesis value contradicts the estimate of less than 'train_departure_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the train departure time
    # any departure time less than 'train_departure_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
