speed_premise = 50
speed_hypothesis = 60

# the hypothesis refers to the driving speed from the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis speed contradicts the estimate of more than 'speed_premise'
    label = "contradiction"
else:
    # the premise gives only a lower limit for the speed
    # any speed greater than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)