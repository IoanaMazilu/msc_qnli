speed_premise = 90
speed_hypothesis = 90

# the hypothesis refers to the speed of Xavier mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the estimate of'speed_hypothesis' contradicts the speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
