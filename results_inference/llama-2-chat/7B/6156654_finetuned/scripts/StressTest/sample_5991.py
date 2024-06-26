gas_cost_premise = 4/gallon
gas_cost_hypothesis = 2/gallon

# the hypothesis refers to the gas cost mentioned in the premise
if gas_cost_premise <= gas_cost_hypothesis:
    # check if the gas cost in the hypothesis contradicts the gas cost in the premise
    label = "contradiction"
else:
    # if the gas cost in the hypothesis does not contradict the gas cost in the premise, we can infer entailment
    label = "entailment"

print(label)
