speed_premise = 10
speed_hypothesis = 90
speed_increase_interval = 12
speed_increase_rate = 20

# the hypothesis talks about the speed of Xavier, the speed increase interval and rate, all referenced in the premise
if speed_hypothesis <= speed_premise:
    # check if the initial speed in the hypothesis contradicts the initial speed in the premise
    label = "contradiction"
elif speed_increase_interval!= 12 or speed_increase_rate!= 20:
    # check if the speed increase interval or rate in the hypothesis contradicts the ones in the premise
    label = "contradiction"
else:
    # the premise gives only a lower limit for the initial speed
    # any initial speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
