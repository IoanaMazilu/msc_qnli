bond_value_premise = 1500
bond_value_hypothesis = 7500

# the hypothesis refers to the value of US saving bonds purchased by Robert, also mentioned in the premise
if bond_value_hypothesis <= bond_value_premise:
    # check if the hypothesis value contradicts the estimate of 'bond_value_premise'
    label = "contradiction"
elif bond_value_hypothesis > bond_value_premise:
    # check if the value of US saving bonds in the hypothesis is greater than the premise value
    label = "entailment"
else:
    # if the hypothesis value and premise value are the same, it is neutral
    label = "neutral"

print(label)
