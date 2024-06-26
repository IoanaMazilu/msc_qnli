speed_premise = 20
speed_hypothesis = 30

# the hypothesis refers to the driving speed between two cities, also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the speed in the hypothesis contradicts the estimate of more than 'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
