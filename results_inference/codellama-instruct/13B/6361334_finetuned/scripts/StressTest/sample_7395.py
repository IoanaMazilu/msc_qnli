distance_premise = 100
distance_hypothesis = 100
speed_premise = 60
speed_hypothesis = 50

# the hypothesis refers to the speed of the journey, which is also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the estimate of'speed_hypothesis' contradicts the speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
