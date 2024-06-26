speed_premise = 30
speed_hypothesis = 50

# the hypothesis talks about the constant speed of driving from City A to City B, also referenced in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed less than'speed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
