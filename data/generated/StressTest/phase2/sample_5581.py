# Premise: A train leaves Delhi at more than 1 a.
# Hypothesis: A train leaves Delhi at 9 a.
# Golden Label: neutral

train_departure_time_premise = 1
train_departure_time_hypothesis = 9

# the hypothesis refers to the train departure time mentioned in the premise
if train_departure_time_hypothesis <= train_departure_time_premise:
    # check if the departure time in the hypothesis contradicts the estimate of 'more than 1 a' in the premise
    label = "contradiction"
else:
    # the premise provides only an estimate for the train departure time
    # any departure time greater than 'train_departure_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

