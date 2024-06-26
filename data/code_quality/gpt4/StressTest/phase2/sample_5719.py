average_speed_premise = 83
average_speed_hypothesis = 43

# the hypothesis refers to the average speed of Ganesh from X to Y mentioned in the premise
if average_speed_hypothesis >= average_speed_premise:
    # check if the speed in the hypothesis contradicts the estimate of less than 'average_speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed less than 'average_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
