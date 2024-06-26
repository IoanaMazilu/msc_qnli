track_length_premise = 600
track_length_hypothesis = 500

# the hypothesis talks about the length of the track, which is also mentioned in the premise
if track_length_hypothesis!= track_length_premise:
    # check if the length of the track in the hypothesis contradicts the length of the track in the premise
    label = "contradiction"
else:
    # if the length of the track in the hypothesis matches the length of the track in the premise, we can infer entailment
    label = "entailment"

print(label)
