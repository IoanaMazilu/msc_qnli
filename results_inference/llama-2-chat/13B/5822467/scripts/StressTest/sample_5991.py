gas_cost_premise = 4
gas_cost_hypothesis = 2

# the hypothesis refers to the cost of gas and the number of miles Dan's car can go
if gas_cost_hypothesis > gas_cost_premise:
    # check if the estimate of 'gas_cost_hypothesis' contradicts the cost of gas reported in the premise
    label = "contradiction"
elif gas_cost_premise!= gas_cost_hypothesis:
    # check if the cost of gas in the hypothesis contradicts the cost of gas reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
