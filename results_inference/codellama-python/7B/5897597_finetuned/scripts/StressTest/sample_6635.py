train_departure_premise = 9
train_departure_hypothesis = 1

# the hypothesis refers to the departure time of the train mentioned in the premise
if train_departure_hypothesis!= train_departure_premise:
    # check if the departure time in the hypothesis contradicts the departure time reported in the premise
    label = "contradiction"
else:
    # if the departure time in the hypothesis does not contradict the departure time in the premise, we can infer entailment
    label = "entailment"

print(label)
