gas_cost_premise = 2
gas_cost_hypothesis = 4
miles_premise = 42

# the hypothesis talks about the cost of gas and the number of miles Dan's car can go
if gas_cost_hypothesis > gas_cost_premise:
    # the hypothesis contradicts the premise, as the cost of gas is higher in the hypothesis than in the premise
    label = "contradiction"
elif miles_premise!= miles_hypothesis:
    # the number of miles reported in the hypothesis does not match the number of miles reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
