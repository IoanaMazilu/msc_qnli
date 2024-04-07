# Premise: The pilot of a small aircraft with a more than 10-gallon fuel tank wants to fly to Cleveland, which is 480 miles away.
# Hypothesis: The pilot of a small aircraft with a 40-gallon fuel tank wants to fly to Cleveland, which is 480 miles away.
# Golden Label: neutral

fuel_tank_premise = 10
fuel_tank_hypothesis = 40
distance_to_cleveland_premise = 480
distance_to_cleveland_hypothesis = 480

# the hypothesis refers to the size of the fuel tank and the distance to Cleveland mentioned in the premise
if fuel_tank_hypothesis <= fuel_tank_premise:
    # check if the size of 'fuel_tank_hypothesis' contradicts the estimate of more than 'fuel_tank_premise'
    label = "contradiction"
elif distance_to_cleveland_hypothesis != distance_to_cleveland_premise:
    # check if the distance to Cleveland in the hypothesis contradicts the distance to Cleveland reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of the fuel tank
    # any size of the fuel tank greater than 'fuel_tank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

