speed_premise = 90
speed_hypothesis = 100
time_interval = 12

# the hypothesis refers to the speed and time interval mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed, any speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
