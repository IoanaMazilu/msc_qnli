speed_premise = 10
speed_hypothesis = 90
increase_speed_premise = 20
increase_speed_hypothesis = 20

# the hypothesis refers to the initial speed and the speed increase rate of Xavier mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the initial speed in the hypothesis contradicts the estimate of more than'speed_premise' kmph
    label = "contradiction"
elif increase_speed_hypothesis!= increase_speed_premise:
    # check if the speed increase rate in the hypothesis contradicts the speed increase rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the initial speed
    # any initial speed greater than'speed_premise' kmph is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
