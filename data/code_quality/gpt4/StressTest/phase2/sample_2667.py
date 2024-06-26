train_departure_premise = 9
train_departure_hypothesis = 3

# the hypothesis refers to the departure time of a train mentioned in the premise
if train_departure_premise <= train_departure_hypothesis:
    # check if the 'train_departure_hypothesis' contradicts the departure time stated in the premise
    label = "contradiction"
else:
    # the hypothesis value does not contradict the premise value, but it cannot be directly entailed either
    label = "neutral"

print(label)
