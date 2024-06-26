train_departure_premise = 9
train_departure_hypothesis = 4

# the hypothesis refers to the train departure time mentioned in the premise
if train_departure_premise <= train_departure_hypothesis:
    # check if the 'train_departure_premise' contradicts the estimate of more than 'train_departure_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
