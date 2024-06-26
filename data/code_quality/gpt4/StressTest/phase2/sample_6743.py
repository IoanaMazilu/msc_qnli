speed_premise = 30
speed_hypothesis = 30

# the hypothesis refers to the speed Ed drives at, which is also mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis value contradicts the premise of driving less than 'speed_premise'
    label = "contradiction"
else:
    # the hypothesis value is less than the premise value
    # any speed less than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
