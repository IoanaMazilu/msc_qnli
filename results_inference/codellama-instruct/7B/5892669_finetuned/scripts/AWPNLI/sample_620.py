gas_premise = 20.0
gas_can_premise = 5.0
gas_can_hypothesis = 4.0

# the hypothesis refers to the number of gas cans needed, which can be computed from the premise
# compute the number of gas cans needed in the premise
gas_can_needed_premise = gas_premise / gas_can_premise
if gas_can_hypothesis!= gas_can_needed_premise:
    # check if the number of gas cans needed in the hypothesis contradicts the number of gas cans needed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
