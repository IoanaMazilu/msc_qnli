# Premise: The pilot of a small aircraft with a 40-gallon fuel tank wants to fly to Cleveland, which is 480 miles away.
# Hypothesis: The pilot of a small aircraft with a 50-gallon fuel tank wants to fly to Cleveland, which is 480 miles away.
# Golden Label: contradiction

fuel_tank_premise = 40
fuel_tank_hypothesis = 50
distance_premise = 480
distance_hypothesis = 480

# the hypothesis refers to the fuel tank capacity and distance mentioned in the premise
if fuel_tank_hypothesis < fuel_tank_premise:
    # check if the capacity of 'fuel_tank_hypothesis' contradicts the fuel tank capacity in the premise
    label = "contradiction"
elif distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

