bond_denomination_premise = [50, 100]
bond_denomination_hypothesis = [10, 100]

# the hypothesis refers to the denomination of the bonds mentioned in the premise
if bond_denomination_hypothesis not in bond_denomination_premise:
    # check if the denomination of the bonds in the hypothesis contradicts the denomination of the bonds in the premise
    label = "contradiction"
else:
    # if the denomination of the bonds in the hypothesis does not contradict the denomination of the bonds in the premise, we can infer entailment
    label = "entailment"

print(label)
