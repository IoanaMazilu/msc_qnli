train_departure_premise = 12
train_departure_hypothesis = 12

# the hypothesis refers to the time of departure of the train mentioned in the premise
if train_departure_hypothesis >= train_departure_premise:
    # check if the hypothesis value contradicts the exact time of departure in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
