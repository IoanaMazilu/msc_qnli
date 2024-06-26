speed_premise = 4
speed_hypothesis = 9

# the hypothesis specifies Lindy's speed, also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the speed in the hypothesis contradicts the estimated speed from the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
