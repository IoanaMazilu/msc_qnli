train_departure_premise = 82
train_departure_hypothesis = 12

# the hypothesis refers to the time of departure of the train, mentioned in the premise
if train_departure_hypothesis >= train_departure_premise:
    # check if the hypothesis value contradicts the estimate of less than 'train_departure_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of departure
    # any time of departure less than 'train_departure_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
