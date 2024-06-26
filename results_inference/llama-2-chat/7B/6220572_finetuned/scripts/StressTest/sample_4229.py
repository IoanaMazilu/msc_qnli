speed_premise = 30
speed_hypothesis = 30

# the hypothesis refers to the constant speed of driving from City A to City B mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the estimate of'speed_hypothesis' contradicts the constant speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed less than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
