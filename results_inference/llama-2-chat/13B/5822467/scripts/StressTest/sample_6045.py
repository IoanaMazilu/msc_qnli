fuel_tank_premise = 40
fuel_tank_hypothesis = 50
distance_to_cleveland = 480

# the hypothesis refers to the fuel tank capacity and the distance to be flown
if fuel_tank_hypothesis <= fuel_tank_premise:
    # check if the estimate of 'fuel_tank_hypothesis' contradicts the fuel tank capacity reported in the premise
    label = "contradiction"
elif fuel_tank_hypothesis > distance_to_cleveland:
    # check if the hypothesis value contradicts the distance to be flown
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
