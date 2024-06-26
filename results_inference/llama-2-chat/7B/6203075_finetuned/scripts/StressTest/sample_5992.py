gas_cost_premise = 2/gallon
gas_cost_hypothesis = 4/gallon

# the hypothesis refers to the cost of gas, which is also mentioned in the premise
if gas_cost_hypothesis < gas_cost_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif gas_cost_hypothesis == gas_cost_premise:
    # check if the hypothesis value is equal to the premise
    label = "neutral"
else:
    # if the hypothesis value is greater than the premise, it does not contradict the premise
    label = "entailment"

print(label)
