track_length_premise = 600
track_length_hypothesis = 500

# the hypothesis refers to the length of the track mentioned in the premise
if track_length_hypothesis!= track_length_premise:
    # check if the length of the track in the hypothesis contradicts the length of the track reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
