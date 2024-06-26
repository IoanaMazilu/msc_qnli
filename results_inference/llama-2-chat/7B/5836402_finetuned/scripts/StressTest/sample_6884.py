bond_denomination_premise = 50
bond_denomination_hypothesis = 70

# the hypothesis refers to the bond denomination which is also mentioned in the premise
if bond_denomination_hypothesis <= bond_denomination_premise:
    # check if the hypothesis value contradicts the estimate of 'bond_denomination_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the bond denomination
    # any denomination greater than 'bond_denomination_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
