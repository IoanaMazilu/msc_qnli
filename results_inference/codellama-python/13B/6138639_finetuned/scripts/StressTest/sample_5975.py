distance_travelled_premise = 8 + 20
distance_travelled_hypothesis = 6 + 20
speed_premise = 40
speed_hypothesis = 40
stop_time_premise = 11
stop_time_hypothesis = 11

# the hypothesis refers to the distance travelled, speed and stop time mentioned in the premise
if distance_travelled_hypothesis!= distance_travelled_premise:
    # check if the distance travelled in the hypothesis contradicts the distance travelled in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif stop_time_hypothesis!= stop_time_premise:
    # check if the stop time in the hypothesis contradicts the stop time in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
