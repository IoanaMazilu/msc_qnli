track_length_premise = 200
track_length_hypothesis = 600

# the hypothesis refers to the length of the track mentioned in the premise
if track_length_premise <= track_length_hypothesis:
    # check if the estimate of 'track_length_hypothesis' contradicts the length of the track in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
