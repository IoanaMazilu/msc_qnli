# Premise: When the river is running at 2 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Hypothesis: When the river is running at less than 4 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Golden Label: entailment

river_speed_premise = 2
river_speed_hypothesis = 4
row_time_premise = 1
row_time_hypothesis = 1

# the hypothesis refers to the speed of the river and the time it takes the rower to row to Big Rock and back, both mentioned in the premise
if river_speed_hypothesis <= river_speed_premise:
    # check if the hypothesis value contradicts the river speed stated in the premise
    label = "contradiction"
elif row_time_hypothesis != row_time_premise:
    # check if the rowing time in the hypothesis contradicts the rowing time stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

