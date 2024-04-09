train_time_premise = 7 * 24 + 1
train_time_hypothesis = 6 * 24 + 1

# the hypothesis refers to the time required by a train to cover a certain distance, which is also mentioned in the premise
if train_time_premise <= train_time_hypothesis:
    # check if the estimate of 'train_time_hypothesis' contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
