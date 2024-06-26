train_departure_time_premise = 9
train_departure_time_hypothesis = 1

# the hypothesis refers to the train departure time mentioned in the premise
if train_departure_time_premise!= train_departure_time_hypothesis:
    # check if the departure time in the hypothesis contradicts the departure time reported in the premise
    label = "contradiction"
else:
    # if the departure times do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
