gas_cost_premise = 4
gas_cost_hypothesis = 2
gas_amount = 42

# the hypothesis refers to the cost of gas mentioned in the premise
if gas_cost_hypothesis >= gas_cost_premise:
    # check if the estimate of 'gas_cost_hypothesis' contradicts the cost of gas in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
