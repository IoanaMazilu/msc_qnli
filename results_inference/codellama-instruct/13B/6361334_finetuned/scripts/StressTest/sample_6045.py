fuel_tank_premise = 40
fuel_tank_hypothesis = 50
distance_premise = 480
distance_hypothesis = 480

# the hypothesis refers to the fuel tank size and the distance to fly, both mentioned in the premise
if fuel_tank_hypothesis >= fuel_tank_premise:
    # check if the estimate of 'fuel_tank_hypothesis' contradicts the fuel tank size in the premise
    label = "contradiction"
elif distance_hypothesis!= distance_premise:
    # check if the distance to fly in the hypothesis contradicts the distance to fly reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
