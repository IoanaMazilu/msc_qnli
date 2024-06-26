river_speed_premise = 2
river_speed_hypothesis = 1
rowing_time_premise = 1
rowing_time_hypothesis = 1

# the hypothesis refers to the river speed mentioned in the premise
if river_speed_hypothesis <= river_speed_premise:
    # check if the estimate of 'river_speed_hypothesis' contradicts the river speed in the premise
    label = "contradiction"
elif rowing_time_hypothesis!= rowing_time_premise:
    # check if the rowing time in the hypothesis contradicts the rowing time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
