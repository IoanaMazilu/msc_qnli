fuel_tank_capacity_premise = 10
fuel_tank_capacity_hypothesis = 40
distance_to_cleveland_premise = 520
distance_to_cleveland_hypothesis = 520

# the hypothesis refers to the capacity of the fuel tank and the distance to Cleveland mentioned in the premise
if fuel_tank_capacity_hypothesis <= fuel_tank_capacity_premise:
    # check if the value of 'fuel_tank_capacity_hypothesis' contradicts the estimate of more than 'fuel_tank_capacity_premise'
    label = "contradiction"
elif distance_to_cleveland_hypothesis != distance_to_cleveland_premise:
    # check if the distance to Cleveland in the hypothesis contradicts the distance to Cleveland reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the fuel tank capacity
    # any fuel tank capacity greater than 'fuel_tank_capacity_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
