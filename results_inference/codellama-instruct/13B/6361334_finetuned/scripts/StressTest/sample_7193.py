train_departure_premise = 12
train_departure_hypothesis = 12

# the hypothesis refers to the time of departure of the train, mentioned in the premise
if train_departure_hypothesis >= train_departure_premise:
    # check if the hypothesis value contradicts the time of departure in the premise
    label = "contradiction"
else:
    # the premise gives an exact time of departure
    # any time of departure less than 'train_departure_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
