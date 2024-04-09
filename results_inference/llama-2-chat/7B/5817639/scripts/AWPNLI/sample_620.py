gas_premise = 20.0
gas_hypothesis = 4.0

# the hypothesis refers to the number of gas cans, which is also mentioned in the premise
# compute the total number of gallons in the premise
total_gas_premise = gas_premise / 5.0

# check if the number of gas cans in the hypothesis contradicts the number of gas cans from the premise
if gas_hypothesis!= total_gas_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
