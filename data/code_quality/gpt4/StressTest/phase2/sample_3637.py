train_departure_premise = 6
train_departure_hypothesis = 9

# the hypothesis refers to the departure time of a train mentioned in the premise
if train_departure_hypothesis <= train_departure_premise:
    # check if the hypothesis value contradicts the estimate of more than 'train_departure_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the departure time
    # any departure time greater than 'train_departure_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
