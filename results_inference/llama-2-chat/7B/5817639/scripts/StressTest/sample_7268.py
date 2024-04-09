track_length_premise = 600
track_length_hypothesis = 500

# the hypothesis refers to the length of the track mentioned in the premise
if track_length_hypothesis <= track_length_premise:
    # check if the hypothesis value contradicts the estimate of 'track_length_premise'
    label = "contradiction"
elif track_length_hypothesis > track_length_premise:
    # check if the length of the track in the hypothesis is greater than the estimate in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
