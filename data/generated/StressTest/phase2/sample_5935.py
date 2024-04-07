# Premise: The pilot of a small aircraft with a more than 20-gallon fuel tank wants to fly to Cleveland, which is 480 miles away.
# Hypothesis: The pilot of a small aircraft with a 60-gallon fuel tank wants to fly to Cleveland, which is 480 miles away.
# Golden Label: neutral

fuel_tank_capacity_premise = 20
fuel_tank_capacity_hypothesis = 60
distance_to_cleveland_premise = 480
distance_to_cleveland_hypothesis = 480

# the hypothesis refers to the capacity of the fuel tank and the distance to Cleveland mentioned in the premise
if fuel_tank_capacity_hypothesis <= fuel_tank_capacity_premise:
    # check if the 'fuel_tank_capacity_hypothesis' contradicts the premise that the fuel tank capacity is more than 'fuel_tank_capacity_premise'
    label = "contradiction"
elif distance_to_cleveland_hypothesis != distance_to_cleveland_premise:
    # check if the distance to Cleveland in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the fuel tank capacity
    # any fuel tank capacity greater than 'fuel_tank_capacity_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

