gas_cost_premise = 4
gas_cost_hypothesis = 2

# the hypothesis talks about the cost of gas, which is also mentioned in the premise
if gas_cost_hypothesis <= gas_cost_premise:
    # check if the hypothesis value contradicts the estimate of gas cost in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the cost of gas
    # any cost of gas greater than $2/gallon is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
