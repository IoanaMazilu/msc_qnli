river_speed_premise = 2
river_speed_hypothesis = 1
rowing_time_premise = 1
rowing_time_hypothesis = 1

# the hypothesis refers to the river speed and the rower's travel time mentioned in the premise
if river_speed_hypothesis <= river_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'river_speed_premise'
    label = "contradiction"
elif rowing_time_hypothesis!= rowing_time_premise:
    # check if the number of rowing hours in the hypothesis contradicts the number of rowing hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
