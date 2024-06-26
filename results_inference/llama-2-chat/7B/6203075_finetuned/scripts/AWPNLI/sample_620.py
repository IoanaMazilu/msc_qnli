gas_to_fill_premise = 20.0
gas_cans_needed_hypothesis = 4.0

# the hypothesis refers to the number of gas cans needed, which can be inferred from the premise
# compute the number of gas cans needed from the premise
gas_cans_needed_premise = gas_to_fill_premise / 5.0
if gas_cans_needed_hypothesis!= gas_cans_needed_premise:
    # check if the number of gas cans needed in the hypothesis contradicts the number of gas cans needed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
