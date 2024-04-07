# Premise: When the river is running at less than 3 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Hypothesis: When the river is running at 1 km/h, it takes the rower 1 hour to row to Big Rock and back.
# Golden Label: neutral

river_speed_premise = 3
river_speed_hypothesis = 1
rowing_time_premise = 1
rowing_time_hypothesis = 1

# the hypothesis refers to the speed of the river and the rowing time mentioned in the premise
if river_speed_hypothesis > river_speed_premise:
    # check if the river speed in the hypothesis contradicts the maximum speed given in the premise
    label = "contradiction"
elif rowing_time_hypothesis != rowing_time_premise:
    # check if the rowing time in the hypothesis contradicts the rowing time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

