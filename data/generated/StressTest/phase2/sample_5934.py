# Premise: The pilot of a small aircraft with a 60-gallon fuel tank wants to fly to Cleveland, which is 480 miles away.
# Hypothesis: The pilot of a small aircraft with a more than 20-gallon fuel tank wants to fly to Cleveland, which is 480 miles away.
# Golden Label: entailment

fuel_tank_premise = 60
fuel_tank_hypothesis = 20
destination_premise = 480
destination_hypothesis = 480

# The hypothesis refers to the size of the fuel tank and the destination mentioned in the premise
if fuel_tank_hypothesis >= fuel_tank_premise:
    # Check if the estimate of 'fuel_tank_hypothesis' contradicts the size of the fuel tank in the premise
    label = "contradiction"
elif destination_hypothesis != destination_premise:
    # Check if the destination stated in the hypothesis contradicts the destination mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

