gas_cost_premise = 2/gallon
gas_cost_hypothesis = 4/gallon

# The hypothesis refers to the cost of gas, which is also mentioned in the premise
if gas_cost_hypothesis >= gas_cost_premise:
    # The hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # If the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
