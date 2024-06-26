train_departure_premise = 9
train_departure_hypothesis = 8

# the hypothesis talks about a train's departure time from Delhi, which is also mentioned in the premise
if train_departure_premise <= train_departure_hypothesis:
    # check if the 'train_departure_premise' contradicts the estimate of more than 'train_departure_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact time of departure
    # if the departure time in the hypothesis is less than that in the premise, it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
