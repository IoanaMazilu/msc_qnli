bond_denomination_premise = 70
bond_denomination_hypothesis = 50

# the hypothesis refers to the denomination of the bonds mentioned in the premise
if bond_denomination_hypothesis >= bond_denomination_premise:
    # check if the denomination of 'bond_denomination_hypothesis' contradicts the premise
    label = "contradiction"
else:
    # the premise gives an upper limit for the denomination of the bonds
    # any denomination less than 'bond_denomination_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
