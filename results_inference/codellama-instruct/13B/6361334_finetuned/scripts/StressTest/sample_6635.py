train_departure_premise = 9
train_departure_hypothesis = 1

# the hypothesis refers to the time of departure of a train from Delhi, which is also mentioned in the premise
if train_departure_hypothesis <= train_departure_premise:
    # check if the estimate of 'train_departure_hypothesis' contradicts the time of departure in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
