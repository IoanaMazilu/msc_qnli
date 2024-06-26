average_speed_premise = 4
average_speed_hypothesis = 3

# the hypothesis refers to the average speed of Murali from A to C mentioned in the premise
if average_speed_hypothesis <= average_speed_premise:
    # check if the estimate of 'average_speed_hypothesis' contradicts the average speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed
    # any average speed greater than 'average_speed_premise' but less than 'average_speed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
