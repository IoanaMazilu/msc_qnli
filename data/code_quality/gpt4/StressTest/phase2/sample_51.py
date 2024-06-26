track_length_premise = 600
track_length_hypothesis = 800

# the hypothesis refers to the length of the running track in the premise
if track_length_premise > track_length_hypothesis:
    # check if the track length in the premise contradicts the estimate of less than 'track_length_hypothesis'
    label = "contradiction"
elif track_length_premise != track_length_hypothesis:
    # check if the track length in the premise contradicts the exact length of 'track_length_hypothesis'
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
