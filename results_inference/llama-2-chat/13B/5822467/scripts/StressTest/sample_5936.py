# Define variables for the numerical entities in the premise and hypothesis
fuel_tank_premise = 60
distance_premise = 480

# Define variables for the numerical entities in the hypothesis
fuel_tank_hypothesis = "more than 60"

# Extract the numerical values from the hypothesis
fuel_tank_hypothesis_value = int(fuel_tank_hypothesis.split(" ")[0])

# Perform calculations and compare the values
if fuel_tank_hypothesis_value > distance_premise:
    # The hypothesis value is greater than the distance, which is consistent with the premise
    label = "neutral"
elif fuel_tank_hypothesis_value <= distance_premise:
    # The hypothesis value is less than or equal to the distance, which contradicts the premise
    label = "contradiction"
else:
    # The hypothesis value is greater than the distance, but we cannot explicitly entail the hypothesis from the premise
    label = "entailment"

print(label)
