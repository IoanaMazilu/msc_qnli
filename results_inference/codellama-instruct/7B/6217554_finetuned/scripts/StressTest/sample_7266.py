track_length_premise = 600
track_length_hypothesis = 200

# the hypothesis talks about the length of the circular track, referenced also in the premise
if track_length_hypothesis >= track_length_premise:
    # check if the hypothesis value contradicts the length of the track in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
