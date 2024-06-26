river_speed_premise = 2
river_speed_hypothesis = 1.5
rowing_time_premise = 1

# the hypothesis refers to the river speed and the time it takes to row to Big Rock and back
if river_speed_hypothesis <= river_speed_premise:
    # check if the estimate of 'river_speed_hypothesis' contradicts the river speed in the premise
    label = "contradiction"
elif rowing_time_premise!= rowing_time_hypothesis:
    # check if the time it takes to row to Big Rock and back in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
