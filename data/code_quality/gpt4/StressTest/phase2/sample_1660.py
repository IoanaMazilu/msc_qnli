stream_speed_premise = 1
stream_speed_hypothesis = 4

# the hypothesis talks about the speed of the stream which is also mentioned in the premise
if stream_speed_hypothesis <= stream_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'stream_speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of the stream
    # any speed greater than 'stream_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
