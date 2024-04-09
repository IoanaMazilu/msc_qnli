gas_cost_premise = 4
gas_cost_hypothesis = 7
gas_amount = 42

# the hypothesis talks about the cost of gas and the distance a car can go on a certain amount of gas
# both values are also mentioned in the premise
if gas_cost_premise!= gas_cost_hypothesis:
    # check if the cost of gas in the hypothesis contradicts the cost of gas mentioned in the premise
    label = "contradiction"
else:
    # if the cost of gas in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
