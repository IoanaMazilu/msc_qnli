# Premise: A truck uses 60-gallon fuel tank wants to travel to Cleveland, which is 480 miles away.
# Hypothesis: A truck uses 10-gallon fuel tank wants to travel to Cleveland, which is 480 miles away.
# Golden Label: contradiction

fuel_tank_capacity_premise = 60
fuel_tank_capacity_hypothesis = 10
destination_distance_premise = 480
destination_distance_hypothesis = 480

# the hypothesis talks about the fuel tank capacity of a truck and the distance to its destination, mentioned also in the premise
if fuel_tank_capacity_hypothesis != fuel_tank_capacity_premise:
    # check if the fuel tank capacity in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
elif destination_distance_hypothesis != destination_distance_premise:
    # check if the destination distance in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

