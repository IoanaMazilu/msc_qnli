track_length_premise = 600
track_length_hypothesis = 200

# the hypothesis refers to the length of the track mentioned in the premise
if track_length_premise <= track_length_hypothesis:
    # check if the length of the track in the premise contradicts the estimate of more than 'track_length_hypothesis'
    label = "contradiction"
else:
    # if the length of the track in the premise is greater than 'track_length_hypothesis', we can infer entailment
    label = "entailment"

print(label)
