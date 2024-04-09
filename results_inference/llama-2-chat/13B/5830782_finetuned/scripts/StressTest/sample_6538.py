speed_premise = 50
speed_hypothesis = 30

# the hypothesis refers to the speed of Cara's drive mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the speed in the hypothesis contradicts the speed limit in the premise
    label = "contradiction"
else:
    # the premise gives an upper limit for the speed
    # any speed less than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
