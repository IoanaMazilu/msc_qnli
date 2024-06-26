stream_speed_premise = 4
stream_speed_hypothesis = 4

# the hypothesis talks about the speed of a stream, referenced also in the premise
if stream_speed_hypothesis != stream_speed_premise:
    # check if the hypothesis value contradicts the speed of stream mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an exact value for the speed of the stream
    # any value that is equal to 'stream_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
