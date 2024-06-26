gas_cost_premise = 4
gas_cost_hypothesis = 2
miles_car_premise = 42
miles_car_hypothesis = 42

# the hypothesis refers to the cost of gas and the number of miles the car can go on that gas
if gas_cost_hypothesis <= gas_cost_premise:
    # check if the estimate of 'gas_cost_hypothesis' contradicts the cost of gas in the premise
    label = "contradiction"
elif miles_car_hypothesis!= miles_car_premise:
    # check if the number of miles the car can go on the gas in the hypothesis contradicts the number of miles reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
