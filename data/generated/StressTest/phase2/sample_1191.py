# Premise: A train leaves Delhi at 7 a.
# Hypothesis: A train leaves Delhi at less than 8 a.
# Golden Label: entailment

train_departure_time_premise = 7
train_departure_time_hypothesis = 8

# the hypothesis refers to the departure time of the train mentioned in the premise
if train_departure_time_premise >= train_departure_time_hypothesis:
    # check if the estimated 'train_departure_time_hypothesis' contradicts the departure time in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

