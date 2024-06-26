train_departure_premise = 9
train_departure_hypothesis = 4

# the hypothesis refers to the time of departure of a train from Delhi
# the premise mentions the time of departure as 9 a.
if train_departure_hypothesis <= train_departure_premise:
    # check if the estimate of 'train_departure_hypothesis' contradicts the time of departure in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of departure
    # any time of departure greater than 'train_departure_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
