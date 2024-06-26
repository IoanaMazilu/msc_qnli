train_departure_premise = 12
train_departure_hypothesis = 42

# the hypothesis refers to the time of departure of a train mentioned in the premise
if train_departure_hypothesis <= train_departure_premise:
    # check if the hypothesis value contradicts the exact departure time of 'train_departure_premise'
    label = "contradiction"
else:
    # the premise gives an exact time for the departure of the train
    # any time greater than 'train_departure_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
