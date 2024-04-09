train_departure_premise = 9
train_departure_hypothesis = 4

# the hypothesis refers to the train departure time mentioned in the premise
if train_departure_premise <= train_departure_hypothesis:
    # check if the train departure time in the premise contradicts the estimate of 'train_departure_hypothesis'
    label = "contradiction"
else:
    # if the train departure time in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
