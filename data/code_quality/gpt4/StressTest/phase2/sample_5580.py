train_departure_premise = 9
train_departure_hypothesis = 1

# the hypothesis talks about the departure time of a train from Delhi, which is also mentioned in the premise
if train_departure_premise <= train_departure_hypothesis:
    # check if the train departure time in the premise contradicts the hypothesis departure time
    label = "contradiction"
elif train_departure_premise > train_departure_hypothesis:
    # check if the train departure time in the premise entails the hypothesis departure time
    label = "entailment"
else:
    # if the premise does not contradict or entail the hypothesis, the relation is neutral
    label = "neutral"

print(label)
