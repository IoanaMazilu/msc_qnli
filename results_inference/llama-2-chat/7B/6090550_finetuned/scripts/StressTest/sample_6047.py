fuel_tank_premise = 40
fuel_tank_hypothesis = 50
distance_to_cleveland = 480

# the hypothesis talks about the fuel tank capacity of the aircraft, which is not mentioned in the premise
if fuel_tank_hypothesis!= fuel_tank_premise:
    # the hypothesis value is different from the premise value, which is a contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
