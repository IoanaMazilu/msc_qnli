gas_to_put_premise = 20.0
can_capacity_premise = 5.0
cans_needed_hypothesis = 4.0

# the hypothesis refers to the number of gas cans needed, which can be calculated from the premise
# compute the number of gas cans needed in the premise
cans_needed_premise = gas_to_put_premise / can_capacity_premise
if cans_needed_hypothesis != cans_needed_premise:
    # check if the number of gas cans in the hypothesis contradicts the number of gas cans from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
