average_speed_premise = 36
average_speed_hypothesis = 36

# the premise gives an estimate for the average speed of the whole journey
if average_speed_hypothesis <= average_speed_premise:
    # check if the hypothesis value contradicts the estimate of the average speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed, any value less than 36 mph is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)