# Defining the variables
bond_denomination_premise = 50
bond_denomination_hypothesis = 70

# the hypothesis refers to the bond denomination mentioned in the premise
if bond_denomination_premise >= bond_denomination_hypothesis:
    # check if the premise value contradicts the hypothesis estimate of 'less than bond_denomination_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
