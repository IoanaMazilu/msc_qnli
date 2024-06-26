fuel_tank_premise = 40
fuel_tank_hypothesis = 50
distance_to_cleveland_premise = 480
distance_to_cleveland_hypothesis = 480

# the hypothesis refers to the fuel tank capacity and distance to Cleveland mentioned in the premise
if fuel_tank_premise!= fuel_tank_hypothesis:
    # check if the fuel tank capacity in the hypothesis contradicts the fuel tank capacity reported in the premise
    label = "contradiction"
elif distance_to_cleveland_premise!= distance_to_cleveland_hypothesis:
    # check if the distance to Cleveland in the hypothesis contradicts the distance to Cleveland reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
