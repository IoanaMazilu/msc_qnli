train_departure_time_premise = 9
train_departure_time_hypothesis = 4

# the hypothesis refers to the train departure time mentioned in the premise
if train_departure_time_premise <= train_departure_time_hypothesis:
    # check if the estimate of 'train_departure_time_hypothesis' contradicts the train departure time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
