initial_speed_premise = 10
initial_speed_hypothesis = 90
speed_increase_interval_premise = 12
speed_increase_interval_hypothesis = 12
speed_increase_rate_premise = 20
speed_increase_rate_hypothesis = 20

# the hypothesis refers to the initial speed, speed increase interval and rate of Xavier, mentioned in the premise
if initial_speed_hypothesis <= initial_speed_premise:
    # check if the initial speed in the hypothesis contradicts the estimate of more than 'initial_speed_premise'
    label = "contradiction"
elif speed_increase_interval_hypothesis!= speed_increase_interval_premise or speed_increase_rate_hypothesis!= speed_increase_rate_premise:
    # check if the speed increase interval or rate in the hypothesis contradicts the ones reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the initial speed
    # any initial speed greater than 'initial_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
