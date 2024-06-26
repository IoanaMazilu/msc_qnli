bond_denomination_premise = 50
bond_denomination_hypothesis = 70

# the hypothesis refers to the denomination of the bonds mentioned in the premise
if bond_denomination_hypothesis == bond_denomination_premise:
    # check if the denomination in the hypothesis contradicts the denomination in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the denomination of the bonds
    # any denomination different from 'bond_denomination_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
