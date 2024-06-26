bond_denomination_premise = 70
bond_denomination_hypothesis = 100

# the hypothesis talks about the denomination of bonds, which is also referenced in the premise
if bond_denomination_hypothesis < bond_denomination_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif bond_denomination_hypothesis == bond_denomination_premise:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"
else:
    # if the hypothesis value is greater than the premise value, it is consistent with the premise
    label = "entailment"

print(label)
