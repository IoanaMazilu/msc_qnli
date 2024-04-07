# Premise: The pilot of a small aircraft with a 40-gallon fuel tank wants to fly to Cleveland, which is 520 miles away.
# Hypothesis: The pilot of a small aircraft with a more than 40-gallon fuel tank wants to fly to Cleveland, which is 520 miles away.
# Golden Label: contradiction

fuel_tank_capacity_premise = 40
fuel_tank_capacity_hypothesis = 40
distance_to_cleveland_premise = 520
distance_to_cleveland_hypothesis = 520

# the hypothesis refers to the fuel tank capacity of the aircraft and the distance to Cleveland, both mentioned in the premise
if fuel_tank_capacity_hypothesis != fuel_tank_capacity_premise:
    # check if the fuel tank capacity in the hypothesis contradicts the capacity reported in the premise
    label = "contradiction"
elif distance_to_cleveland_hypothesis != distance_to_cleveland_premise:
    # check if the distance to Cleveland in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

