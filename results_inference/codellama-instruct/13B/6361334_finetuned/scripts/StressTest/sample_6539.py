speed_premise = 30
speed_hypothesis = 60

# the hypothesis refers to the speed of the car mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the estimate of'speed_hypothesis' contradicts the speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)