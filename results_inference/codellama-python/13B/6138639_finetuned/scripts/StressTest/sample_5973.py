distance_1_premise = 8
distance_1_hypothesis = 4
distance_2_premise = 20
distance_2_hypothesis = 20
stop_time_premise = 11
stop_time_hypothesis = 11

# the hypothesis refers to the distances and stop time mentioned in the premise
if distance_1_premise <= distance_1_hypothesis:
    # check if the estimate of 'distance_1_hypothesis' contradicts the distance travelled in the premise
    label = "contradiction"
elif stop_time_hypothesis!= stop_time_premise:
    # check if the stop time in the hypothesis contradicts the stop time reported in the premise
    label = "contradiction"
elif distance_2_hypothesis!= distance_2_premise:
    # check if the distance travelled in the hypothesis contradicts the distance travelled reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
