bond_denomination_premise = [70, 100]
bond_denomination_hypothesis = [50, 100]

# the hypothesis refers to the bond denominations mentioned in the premise
if bond_denomination_hypothesis[0] >= bond_denomination_premise[0]:
    # check if the lower bond denomination in the hypothesis contradicts the lower bond denomination in the premise
    label = "contradiction"
elif bond_denomination_hypothesis[1] != bond_denomination_premise[1]:
    # check if the higher bond denomination in the hypothesis contradicts the higher bond denomination mentioned in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are about the same, but the denominations of the bonds vary
    # thus, the relation is neutral because the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise either
    label = "neutral"

print(label)
