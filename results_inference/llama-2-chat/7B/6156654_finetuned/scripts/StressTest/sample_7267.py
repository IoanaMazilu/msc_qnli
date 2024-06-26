track_length_premise = 200
track_length_hypothesis = 600

# the hypothesis talks about the length of the track, which is also mentioned in the premise
if track_length_hypothesis <= track_length_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif track_length_hypothesis > track_length_premise:
    # the premise gives a lower limit for the track length
    # any track length greater than the premise is consistent with the premise, so we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value and the premise value are the same, we can infer neutral
    label = "neutral"

print(label)
