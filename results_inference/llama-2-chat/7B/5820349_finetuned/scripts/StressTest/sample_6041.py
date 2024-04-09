speed_premise = 90
speed_hypothesis = 90
speed_increase_premise = 20
speed_increase_hypothesis = 20
time_premise = 12
time_hypothesis = 12

# the hypothesis refers to the initial speed and the speed increase mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the'speed_hypothesis' contradicts the initial speed in the premise
    label = "contradiction"
elif speed_increase_hypothesis!= speed_increase_premise:
    # check if the speed increase in the hypothesis contradicts the speed increase reported in the premise
    label = "contradiction"
elif time_hypothesis!= time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
