train_time_premise = 7
train_time_hypothesis = 6

# the hypothesis refers to the time required by a train to cover the distance between Chennai and Jammu mentioned in the premise
if train_time_premise <= train_time_hypothesis:
    # check if the estimate of 'train_time_hypothesis' contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
