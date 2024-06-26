gas_cost_premise = 2/gallon
gas_cost_hypothesis = 4/gallon

# the hypothesis talks about the cost of gas, which is also mentioned in the premise
if gas_cost_hypothesis == gas_cost_premise:
    # check if the cost of gas in the hypothesis contradicts the cost of gas in the premise
    label = "contradiction"
else:
    # if the cost of gas in the hypothesis does not contradict the cost of gas in the premise, we can infer entailment
    label = "entailment"

print(label)
