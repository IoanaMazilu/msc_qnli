speed_premise = 80
speed_hypothesis = 40

# the hypothesis refers to the average speed of the trip, which is also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the estimate of'speed_hypothesis' contradicts the speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed, any speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
