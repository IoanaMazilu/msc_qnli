train_departure_premise = 9
train_departure_hypothesis = 4

# the hypothesis refers to the train departure time mentioned in the premise
if train_departure_premise <= train_departure_hypothesis:
    # check if the 'train_departure_hypothesis' contradicts the train departure time in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
