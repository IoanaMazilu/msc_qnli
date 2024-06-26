bond_denomination_premise = 70
bond_denomination_hypothesis = 50

# the hypothesis refers to the denomination of the bonds sold, referenced also in the premise
if bond_denomination_hypothesis <= bond_denomination_premise:
    # check if the hypothesis value contradicts the estimate of 'bond_denomination_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the denomination of the bonds sold
    # any number of bonds sold in a denomination greater than 'bond_denomination_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
