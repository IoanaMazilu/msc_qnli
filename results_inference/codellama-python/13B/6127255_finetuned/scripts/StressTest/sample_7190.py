train_departure_premise = 12
train_departure_hypothesis = 62

# the hypothesis refers to the train departure time mentioned in the premise
if train_departure_hypothesis!= train_departure_premise:
    # check if the train departure time in the hypothesis contradicts the train departure time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
