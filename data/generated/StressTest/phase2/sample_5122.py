# Premise: A boat crossed a lake from East to West at the speed of less than 8 km/h, entered a river and covered twice as much distance going upstream at 4 km/h.
# Hypothesis: A boat crossed a lake from East to West at the speed of 5 km/h, entered a river and covered twice as much distance going upstream at 4 km/h.
# Golden Label: neutral

speed_boat_lake_premise = 8
speed_boat_lake_hypothesis = 5
speed_boat_river_premise = 4
speed_boat_river_hypothesis = 4

# the hypothesis talks about the speed of the boat on a lake and a river, which is also mentioned in the premise
if speed_boat_lake_hypothesis >= speed_boat_lake_premise:
    # check if the speed of the boat on the lake in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif speed_boat_river_hypothesis != speed_boat_river_premise:
    # check if the speed of the boat on the river in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, we can infer entailment
    label = "entailment"

print(label)

