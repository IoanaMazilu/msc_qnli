track_length_premise = 200
track_length_hypothesis = 600

# the hypothesis refers to the length of the track mentioned in the premise
if track_length_premise <= track_length_hypothesis:
    # check if the estimate of 'track_length_hypothesis' contradicts the number of track length in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of the track
    # any length greater than 'track_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
