fuel_tank_premise = 60
fuel_tank_hypothesis = 10
distance_premise = 480
distance_hypothesis = 480

# the hypothesis refers to the size of the fuel tank and the distance to Cleveland mentioned in the premise
if fuel_tank_hypothesis!= fuel_tank_premise:
    # check if the size of the fuel tank in the hypothesis contradicts the size of the fuel tank reported in the premise
    label = "contradiction"
elif distance_hypothesis!= distance_premise:
    # check if the distance to Cleveland in the hypothesis contradicts the distance to Cleveland reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
