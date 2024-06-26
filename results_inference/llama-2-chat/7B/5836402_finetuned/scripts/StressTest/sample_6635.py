train_departure_time_premise = 9
train_departure_time_hypothesis = 1

# the hypothesis refers to the time of departure of a train from Delhi mentioned in the premise
if train_departure_time_premise!= train_departure_time_hypothesis:
    # check if the departure time in the hypothesis contradicts the departure time in the premise
    label = "contradiction"
else:
    # if the departure time in the hypothesis does not contradict the departure time in the premise, we can infer entailment
    label = "entailment"

print(label)
