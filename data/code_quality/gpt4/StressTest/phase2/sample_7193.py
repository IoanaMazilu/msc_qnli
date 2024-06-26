train_departure_premise = 12
train_departure_hypothesis = 12

# the hypothesis tells about the departure time of a train, which is also mentioned in the premise
if train_departure_hypothesis >= train_departure_premise:
    # check if the hypothesis value contradicts the premise of 'train_departure_premise' at 12 noon
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)