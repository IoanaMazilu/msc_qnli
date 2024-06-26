bond_denomination_premise = 70
bond_denomination_hypothesis = 50

# the hypothesis refers to the denomination of the bonds mentioned in the premise
if bond_denomination_hypothesis >= bond_denomination_premise:
    # check if the denomination of the bonds in the hypothesis contradicts the denomination of the bonds in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the denomination of the bonds
    # any denomination less than 'bond_denomination_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
