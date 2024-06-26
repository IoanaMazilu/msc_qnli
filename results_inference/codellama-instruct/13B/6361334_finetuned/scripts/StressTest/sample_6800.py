bond_purchase_premise = 4000
bond_purchase_hypothesis = 5000

# the hypothesis refers to the amount of US saving bonds purchased by Robert
if bond_purchase_hypothesis <= bond_purchase_premise:
    # check if the estimate of 'bond_purchase_hypothesis' contradicts the amount of bonds purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
