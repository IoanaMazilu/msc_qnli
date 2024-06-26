fuel_tank_premise = 60
fuel_tank_hypothesis = 60
distance_to_cleveland = 480

# the hypothesis talks about the fuel tank size, which is also mentioned in the premise
if fuel_tank_hypothesis <= fuel_tank_premise:
    # check if the hypothesis value contradicts the premise of more than 'fuel_tank_premise' gallons
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"

print(label)
