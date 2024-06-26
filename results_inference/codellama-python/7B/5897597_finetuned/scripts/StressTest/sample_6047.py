fuel_tank_premise = 40
fuel_tank_hypothesis = 50
cleveland_distance_premise = 480
cleveland_distance_hypothesis = 480

# the hypothesis refers to the size of the fuel tank and the distance to Cleveland mentioned in the premise
if fuel_tank_premise!= fuel_tank_hypothesis:
    # check if the size of the fuel tank in the hypothesis contradicts the size of the fuel tank reported in the premise
    label = "contradiction"
elif cleveland_distance_hypothesis!= cleveland_distance_premise:
    # check if the distance to Cleveland in the hypothesis contradicts the distance to Cleveland reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
