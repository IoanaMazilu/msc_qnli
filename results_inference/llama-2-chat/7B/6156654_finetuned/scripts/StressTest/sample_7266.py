track_length_premise = 600
track_length_hypothesis = 200

# the hypothesis refers to the length of the track, which is also mentioned in the premise
if track_length_hypothesis <= track_length_premise:
    # check if the length of the track in the hypothesis contradicts the length of the track in the premise
    label = "contradiction"
elif track_length_hypothesis > track_length_premise:
    # if the length of the track in the hypothesis is greater than the length of the track in the premise, it is consistent with the premise
    label = "entailment"
else:
    # if the length of the track in the hypothesis is equal to the length of the track in the premise, it is neutral
    label = "neutral"

print(label)
