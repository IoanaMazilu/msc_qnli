track_length_premise = 200
track_length_hypothesis = 600

# the hypothesis refers to the length of the track mentioned in the premise
if track_length_hypothesis <= track_length_premise:
    # check if the hypothesis value contradicts the estimate of more than 'track_length_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the track length
    # any track length greater than 'track_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
