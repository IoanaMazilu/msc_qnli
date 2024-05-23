bond_denomination_premise = 50
bond_denomination_hypothesis = 70

# the hypothesis talks about the denomination of bonds, referenced also in the premise
if bond_denomination_hypothesis!= bond_denomination_premise:
    # check if the bond denomination in the hypothesis contradicts the bond denomination in the premise
    label = "contradiction"
else:
    # if the bond denomination in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)