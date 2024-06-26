fuel_tank_premise = 60
fuel_tank_hypothesis = 60
distance_to_cleveland = 480

# the hypothesis refers to the size of the fuel tank and the distance to Cleveland mentioned in the premise
if fuel_tank_premise >= fuel_tank_hypothesis:
    # check if the estimate of 'fuel_tank_hypothesis' contradicts the size of the fuel tank in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones
    # we can infer entailment as the premise does not give explicit information about the fuel requirement for the trip
    label = "neutral"

print(label)
