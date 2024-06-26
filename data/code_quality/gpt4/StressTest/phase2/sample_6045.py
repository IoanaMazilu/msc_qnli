fuel_tank_capacity_premise = 40
fuel_tank_capacity_hypothesis = 50
destination_distance_premise = 480
destination_distance_hypothesis = 480

# the hypothesis talks about the fuel tank capacity and the distance to Cleveland
if fuel_tank_capacity_hypothesis <= fuel_tank_capacity_premise:
    # check if the estimate of 'fuel_tank_capacity_hypothesis' contradicts the fuel tank capacity in the premise
    label = "contradiction"
elif destination_distance_hypothesis != destination_distance_premise:
    # check if the distance to Cleveland in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
