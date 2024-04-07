# Premise: A train leaves Delhi at 9 a.
# Hypothesis: A train leaves Delhi at more than 4 a.
# Golden Label: entailment

train_departure_premise = 9
train_departure_hypothesis = 4

# the hypothesis talks about the departure time of a train, referenced also in the premise
if train_departure_premise <= train_departure_hypothesis:
    # check if the premise value contradicts the estimate of more than 'train_departure_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives only an estimate for the departure time
    # any departure time greater than 'train_departure_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)

