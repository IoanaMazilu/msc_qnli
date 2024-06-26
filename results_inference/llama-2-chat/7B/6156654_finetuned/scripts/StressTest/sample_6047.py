fuel_tank_size_premise = 40
fuel_tank_size_hypothesis = 50
distance_to_cleveland_premise = 480
distance_to_cleveland_hypothesis = 480

# the hypothesis refers to the fuel tank size and distance to Cleveland mentioned in the premise
if fuel_tank_size_hypothesis!= fuel_tank_size_premise:
    # check if the fuel tank size in the hypothesis contradicts the fuel tank size mentioned in the premise
    label = "contradiction"
elif distance_to_cleveland_hypothesis!= distance_to_cleveland_premise:
    # check if the distance to Cleveland in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
