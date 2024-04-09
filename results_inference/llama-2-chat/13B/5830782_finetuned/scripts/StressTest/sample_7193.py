train_departure_time_premise = 12
train_departure_time_hypothesis = 12

# the hypothesis refers to the train departure time mentioned in the premise
if train_departure_time_hypothesis >= train_departure_time_premise:
    # check if the hypothesis value contradicts the premise of 'less than 12 noon'
    label = "contradiction"
else:
    # the premise gives an exact time for the train departure
    # any departure time less than 'train_departure_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
