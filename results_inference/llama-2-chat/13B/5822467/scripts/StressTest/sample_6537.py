speed_premise = 30
speed_hypothesis = 50

# the hypothesis refers to the speed at which Cara drives
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific value for the speed, while the hypothesis gives a range
    # any speed less than 50 miles per hour is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
