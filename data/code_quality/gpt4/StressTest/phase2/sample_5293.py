train_departure_premise = 41
train_departure_hypothesis = 11

# the hypothesis is about the departure time of a train, which is also mentioned in the premise
if train_departure_hypothesis >= train_departure_premise:
    # check if the hypothesis value contradicts the estimate of 'less than train_departure_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the departure time
    # any departure time less than 'train_departure_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
