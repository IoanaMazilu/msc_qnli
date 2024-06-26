initial_speed_premise = 90
initial_speed_hypothesis = 90
increase_speed_premise = 20
increase_speed_hypothesis = 20
time_premise = 12
time_hypothesis = 12

# the hypothesis refers to the initial speed, the speed increase and the time interval mentioned in the premise
if initial_speed_premise >= initial_speed_hypothesis:
    # check if the estimate of 'initial_speed_hypothesis' contradicts the initial speed in the premise
    label = "contradiction"
elif increase_speed_premise!= increase_speed_hypothesis:
    # check if the speed increase in the hypothesis contradicts the speed increase reported in the premise
    label = "contradiction"
elif time_premise!= time_hypothesis:
    # check if the time interval in the hypothesis contradicts the time interval reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
