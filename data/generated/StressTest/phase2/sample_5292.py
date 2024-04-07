# Premise: A train leaves Delhi at 11 a.
# Hypothesis: A train leaves Delhi at less than 41 a.
# Golden Label: entailment

train_departure_time_premise = 11
train_departure_time_hypothesis = 41

# the hypothesis talks about the departure time of a train from Delhi, which is also referenced in the premise
if train_departure_time_hypothesis <= train_departure_time_premise:
    # check if 'train_departure_time_hypothesis' contradicts the premise
    label = "contradiction"
elif train_departure_time_hypothesis > train_departure_time_premise:
    # the premise gives an explicit departure time
    # any departure time greater than 'train_departure_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

