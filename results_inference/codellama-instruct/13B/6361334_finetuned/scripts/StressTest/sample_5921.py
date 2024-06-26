average_speed_premise = 80
average_speed_hypothesis = 80

# the hypothesis refers to the average speed of driving from home to the beach and back home
if average_speed_hypothesis <= average_speed_premise:
    # check if the estimate of 'average_speed_hypothesis' contradicts the average speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed
    # any speed greater than 'average_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
