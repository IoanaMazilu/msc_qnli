fuel_tank_premise = 40
fuel_tank_hypothesis = 10
distance_to_cleveland_premise = 520
distance_to_cleveland_hypothesis = 520

# the hypothesis refers to the fuel tank size and distance to Cleveland mentioned in the premise
if fuel_tank_premise <= fuel_tank_hypothesis:
    # check if the estimate of 'fuel_tank_hypothesis' contradicts the size of the fuel tank in the premise
    label = "contradiction"
elif distance_to_cleveland_premise != distance_to_cleveland_hypothesis:
    # check if the distance to Cleveland in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
