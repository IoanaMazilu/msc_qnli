average_speed_premise = 76
average_speed_hypothesis = 36

# the hypothesis talks about the average speed of a journey, which is also referenced in the premise
if average_speed_premise <= average_speed_hypothesis:
    # check if the estimate of 'average_speed_hypothesis' contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed, any value less than or equal to the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
