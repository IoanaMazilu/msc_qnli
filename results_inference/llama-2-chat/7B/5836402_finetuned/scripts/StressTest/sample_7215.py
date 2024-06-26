fuel_tank_capacity_premise = 60
fuel_tank_capacity_hypothesis = 20
distance_cleveland = 480

# the hypothesis refers to the fuel tank capacity and the distance to Cleveland mentioned in the premise
if fuel_tank_capacity_premise >= fuel_tank_capacity_hypothesis:
    # check if the estimate of 'fuel_tank_capacity_hypothesis' contradicts the fuel tank capacity in the premise
    label = "contradiction"
elif distance_cleveland!= fuel_tank_capacity_hypothesis:
    # check if the distance to Cleveland in the hypothesis contradicts the distance to Cleveland reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
