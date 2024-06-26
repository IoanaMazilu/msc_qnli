# Define variables for the numerical entities in the premise and hypothesis
fuel_tank_premise = 40
distance_premise = 480

# Define variables for the numerical entities in the hypothesis
fuel_tank_hypothesis = 50

# Check if the fuel tank in the hypothesis is less than the fuel tank in the premise
if fuel_tank_hypothesis < fuel_tank_premise:
    # Check if the distance to fly to Cleveland is the same in both cases
    if distance_premise == distance_hypothesis:
        # The hypothesis is entailed from the premise
        label = "entailment"
    else:
        # The hypothesis is not entailed from the premise
        label = "contradiction"
else:
    # The hypothesis is not entailed from the premise
    label = "contradiction"

print(label)
