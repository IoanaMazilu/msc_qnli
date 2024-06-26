gas_premise = 20.0
can_capacity_premise = 5.0
cans_hypothesis = 4.0

# the hypothesis refers to the number of gas cans needed, which can be computed from the premise
# compute the total number of gas cans needed from the premise
total_cans_premise = gas_premise / can_capacity_premise
if cans_hypothesis!= total_cans_premise:
    # check if the number of gas cans in the hypothesis contradicts the number of gas cans from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
