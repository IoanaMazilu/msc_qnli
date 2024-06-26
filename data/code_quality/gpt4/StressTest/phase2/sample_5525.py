gas_cost_premise = 4
gas_cost_hypothesis = 1

# both the premise and hypothesis talk about the cost of gas
if gas_cost_premise != gas_cost_hypothesis:
    # check if the gas cost in the hypothesis contradicts the gas cost in the premise
    label = "contradiction"
else:
    # In this case, no specific comparison or calculation is needed as the cost in the premise and hypothesis are directly compared
    label = "neutral"

print(label)
