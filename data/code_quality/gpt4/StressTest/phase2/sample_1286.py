bond_denomination_premise = 50
bond_denomination_hypothesis = 100

# the hypothesis refers to the bond denomination in the premise
if bond_denomination_hypothesis < bond_denomination_premise:
    # check if the bond denomination in the hypothesis contradicts the bond denomination in the premise
    label = "contradiction"
else:
    # the premise gives a specific value for the bond denomination
    # any bond denominations equal or greater than 'bond_denomination_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
