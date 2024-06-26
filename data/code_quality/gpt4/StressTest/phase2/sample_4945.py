river_speed_premise = 4
river_speed_hypothesis = 2
row_duration_premise = 1
row_duration_hypothesis = 1

# the hypothesis refers to the river's speed and the rowing duration mentioned in the premise
if river_speed_hypothesis > river_speed_premise:
    # check if the river's speed in the hypothesis contradicts the river's speed in the premise
    label = "contradiction"
elif row_duration_hypothesis != row_duration_premise:
    # check if the rowing duration in the hypothesis contradicts the rowing duration in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
