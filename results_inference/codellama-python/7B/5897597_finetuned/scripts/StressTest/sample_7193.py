train_departure_time_premise = 12
train_departure_time_hypothesis = 12

# the hypothesis refers to the train departure time mentioned in the premise
if train_departure_time_hypothesis >= train_departure_time_premise:
    # check if the hypothesis value contradicts the exact departure time in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
