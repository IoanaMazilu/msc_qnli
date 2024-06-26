fuel_tank_premise = 60
fuel_tank_hypothesis = 60
distance_premise = 480
distance_hypothesis = 480

# the hypothesis refers to the size of the fuel tank and the distance to fly
if fuel_tank_hypothesis <= fuel_tank_premise:
    # check if the estimate of 'fuel_tank_hypothesis' contradicts the size of the fuel tank in the premise
    label = "contradiction"
elif distance_hypothesis!= distance_premise:
    # check if the distance to fly in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
