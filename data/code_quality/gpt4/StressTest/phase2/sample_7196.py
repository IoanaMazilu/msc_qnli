train_travel_time_premise = 7 * 24 * 60 + 1  # time in minutes
train_travel_time_hypothesis = 7 * 24 * 60 + 1  # time in minutes

# the hypothesis refers to the exact travel time mentioned in the premise
if train_travel_time_hypothesis > train_travel_time_premise:
    # check if the 'train_travel_time_hypothesis' contradicts the exact travel time in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
