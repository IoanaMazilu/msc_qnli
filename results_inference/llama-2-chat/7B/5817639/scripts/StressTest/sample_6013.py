average_speed_premise = 20
average_speed_hypothesis = 60

# the hypothesis talks about the average speed of two drivers, referenced also in the premise
if average_speed_hypothesis <= average_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed
    # any average speed greater than 'average_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
