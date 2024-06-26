speed_premise = 40
speed_hypothesis = 70

# the hypothesis refers to the speed of Bob's car, which is also mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis value contradicts the speed in the premise
    label = "contradiction"
else:
    # the premise gives an exact speed, but the hypothesis gives a lower bound
    # any speed less than'speed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
