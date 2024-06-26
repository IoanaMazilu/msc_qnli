train_departure_premise = 12
train_departure_hypothesis = 42

# the hypothesis refers to the train departure time mentioned in the premise
if train_departure_hypothesis <= train_departure_premise:
    # check if the 'train_departure_hypothesis' contradicts the train departure time in the premise
    label = "contradiction"
elif train_departure_hypothesis > train_departure_premise:
    # check if the train departure time in the hypothesis is greater than the train departure time in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
