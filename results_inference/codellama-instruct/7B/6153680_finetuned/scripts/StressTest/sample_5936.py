fuel_tank_size_premise = 60
fuel_tank_size_hypothesis = 60
distance_to_cleveland = 480

# the hypothesis refers to the fuel tank size and the distance to Cleveland mentioned in the premise
if fuel_tank_size_hypothesis <= fuel_tank_size_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
