fuel_tank_premise = 20
fuel_tank_hypothesis = 60
distance_to_cleveland = 480

# the hypothesis refers to the fuel tank size and distance to Cleveland mentioned in the premise
if fuel_tank_hypothesis <= fuel_tank_premise:
    # check if the hypothesis value contradicts the estimate of more than 'fuel_tank_premise'
    label = "contradiction"
elif distance_to_cleveland!= 480:
    # check if the distance to Cleveland in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
