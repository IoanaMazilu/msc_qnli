gas_cost_premise = 2
gas_cost_hypothesis = 4
miles_per_gallon = 42

# the hypothesis refers to the cost of gas and the number of miles per gallon, both mentioned in the premise
if gas_cost_hypothesis <= gas_cost_premise:
    # check if the estimate of 'gas_cost_hypothesis' contradicts the cost of gas in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the cost of gas
    # any cost of gas greater than 'gas_cost_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
