track_length_premise = 600
track_length_hypothesis = 200

# the hypothesis refers to the length of the track mentioned in the premise
if track_length_premise <= track_length_hypothesis:
    # check if the estimate of 'track_length_hypothesis' contradicts the length of the track in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
