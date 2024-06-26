gas_cost_premise = 2
gas_cost_hypothesis = 4

# the hypothesis talks about the cost of gas, referenced also in the premise
if gas_cost_hypothesis <= gas_cost_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gas_cost_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the cost of gas
    # any cost of gas greater than 'gas_cost_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
