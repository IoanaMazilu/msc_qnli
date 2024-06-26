speed_premise = 10
speed_hypothesis = 90
increase_speed_premise = 20
increase_speed_hypothesis = 20
time_premise = 12
time_hypothesis = 12

# the hypothesis refers to the speed and time of Xavier's movement mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the speed in the hypothesis contradicts the estimate of more than'speed_premise'
    label = "contradiction"
elif increase_speed_hypothesis!= increase_speed_premise:
    # check if the increase in speed in the hypothesis contradicts the increase in speed reported in the premise
    label = "contradiction"
elif time_hypothesis!= time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
