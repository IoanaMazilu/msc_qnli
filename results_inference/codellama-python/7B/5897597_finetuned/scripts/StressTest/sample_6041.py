initial_speed_premise = 90
initial_speed_hypothesis = 90
speed_increase_interval_premise = 12
speed_increase_interval_hypothesis = 12
speed_increase_rate_premise = 20
speed_increase_rate_hypothesis = 20

# the hypothesis refers to the initial speed, speed increase interval and speed increase rate mentioned in the premise
if initial_speed_hypothesis <= initial_speed_premise:
    # check if the hypothesis value contradicts the initial speed in the premise
    label = "contradiction"
elif speed_increase_interval_hypothesis!= speed_increase_interval_premise:
    # check if the speed increase interval in the hypothesis contradicts the speed increase interval reported in the premise
    label = "contradiction"
elif speed_increase_rate_hypothesis!= speed_increase_rate_premise:
    # check if the speed increase rate in the hypothesis contradicts the speed increase rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
