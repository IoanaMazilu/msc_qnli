gas_premise = 20.0
gas_cans_hypothesis = 4.0

# the hypothesis refers to the number of gas cans needed, which is also mentioned in the premise
# compute the number of gas cans needed from the premise
gas_cans_premise = gas_premise / gas_cans_hypothesis
if gas_cans_premise!= gas_cans_hypothesis:
    # check if the number of gas cans from the hypothesis contradicts the number of gas cans from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
