fuel_tank_premise = 20
fuel_tank_hypothesis = 60
distance_premise = 480
distance_hypothesis = 480

# the hypothesis refers to the fuel tank size and distance mentioned in the premise
if fuel_tank_hypothesis <= fuel_tank_premise:
    # check if the estimate of 'fuel_tank_hypothesis' contradicts the number of gallons in the premise
    label = "contradiction"
elif distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
