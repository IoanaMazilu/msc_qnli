fuel_tank_capacity_premise = 60
fuel_tank_capacity_hypothesis = 20
distance_to_cleveland_premise = 480
distance_to_cleveland_hypothesis = 480

# the hypothesis refers to the fuel tank usage and distance to Cleveland mentioned in the premise
if fuel_tank_capacity_premise <= fuel_tank_capacity_hypothesis:
    # check if the estimate of 'fuel_tank_capacity_hypothesis' contradicts the fuel tank usage in the premise
    label = "contradiction"
elif distance_to_cleveland_hypothesis != distance_to_cleveland_premise:
    # check if the distance to Cleveland in the hypothesis contradicts the distance to Cleveland reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
