average_speed_premise = 2
average_speed_hypothesis = 8

# the hypothesis talks about the average speed of Murali from A to C, referenced also in the premise
if average_speed_premise <= average_speed_hypothesis:
    # check if the hypothesis value contradicts the estimate of average speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed
    # any average speed value greater than 'average_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
