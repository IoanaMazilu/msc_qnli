stream_speed_premise = 4
stream_speed_hypothesis = 1

# the hypothesis refers to the speed of the stream mentioned in the premise
if stream_speed_premise <= stream_speed_hypothesis:
    # check if the estimate of 'stream_speed_hypothesis' contradicts the speed of the stream in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
