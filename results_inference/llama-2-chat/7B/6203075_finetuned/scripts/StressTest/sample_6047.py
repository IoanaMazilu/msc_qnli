fuel_tank_premise = 40
fuel_tank_hypothesis = 50
distance_to_cleveland_premise = 480
distance_to_cleveland_hypothesis = 480

# the hypothesis talks about the fuel tank size and the distance to Cleveland, both referenced in the premise
if fuel_tank_hypothesis!= fuel_tank_premise:
    # check if the fuel tank size in the hypothesis contradicts the fuel tank size in the premise
    label = "contradiction"
elif distance_to_cleveland_hypothesis!= distance_to_cleveland_premise:
    # check if the distance to Cleveland in the hypothesis contradicts the distance to Cleveland in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)