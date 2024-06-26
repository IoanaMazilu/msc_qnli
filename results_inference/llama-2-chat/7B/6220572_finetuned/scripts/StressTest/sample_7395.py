speed_premise = 60
speed_hypothesis = 50

# the hypothesis refers to the speed of driving mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
