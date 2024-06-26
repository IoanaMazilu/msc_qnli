bond_denomination_premise = 50
bond_denomination_hypothesis = 10

# the hypothesis talks about the denomination of bonds sold, referenced also in the premise
if bond_denomination_hypothesis == bond_denomination_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only a specific denomination for the bonds
    # any other denomination is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
