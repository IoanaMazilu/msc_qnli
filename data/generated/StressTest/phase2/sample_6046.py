# Premise: The pilot of a small aircraft with a less than 50-gallon fuel tank wants to fly to Cleveland, which is 480 miles away.
# Hypothesis: The pilot of a small aircraft with a 40-gallon fuel tank wants to fly to Cleveland, which is 480 miles away.
# Golden Label: neutral

fuel_tank_capacity_premise = 50
fuel_tank_capacity_hypothesis = 40
destination_distance_premise = 480
destination_distance_hypothesis = 480

# the hypothesis talks about the capacity of a fuel tank and a distance to a destination referenced also in the premise
if fuel_tank_capacity_hypothesis >= fuel_tank_capacity_premise:
    # check if the fuel tank capacity in the hypothesis contradicts the premise's estimate of less than 'fuel_tank_capacity_premise'
    label = "contradiction"
elif destination_distance_hypothesis != destination_distance_premise:
    # check if the distance to the destination in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

