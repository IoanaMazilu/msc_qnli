track_length_premise = 600
track_length_hypothesis = 800

# the hypothesis refers to the length of the track on which Arjun and Bhishma are running, same as the premise
if track_length_premise > track_length_hypothesis:
    # check if the track length in the premise contradicts the estimate of less than 'track_length_hypothesis' in the hypothesis
    label = "contradiction"
elif track_length_premise == track_length_hypothesis:
    # the premise mentions the exact length of the track
    # if the length of the track in the hypothesis is equal to 'track_length_premise', it contradicts the estimate of less than 'track_length_hypothesis'
    label = "contradiction"
else:
    # if the track length in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
