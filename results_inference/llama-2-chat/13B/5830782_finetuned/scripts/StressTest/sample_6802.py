bond_denomination_premise = 70
bond_denomination_hypothesis = 50

# the hypothesis refers to the denomination of bonds mentioned in the premise
if bond_denomination_hypothesis >= bond_denomination_premise:
    # check if the hypothesis value contradicts the premise that bonds are sold in less than 'bond_denomination_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the denomination of bonds
    # any denomination less than 'bond_denomination_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
