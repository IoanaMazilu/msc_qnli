speed_premise = 40
speed_hypothesis = 10

# the hypothesis refers to the speed at which Bob drives from City A to City B, which is also mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis value contradicts the speed in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the speed, but any speed less than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
