bond_value_premise = 1500
bond_value_hypothesis = 6500

# the hypothesis refers to the value of US saving bonds purchased by Robert, which is also mentioned in the premise
if bond_value_premise >= bond_value_hypothesis:
    # check if the estimate of 'bond_value_hypothesis' contradicts the value of US saving bonds purchased by Robert in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
