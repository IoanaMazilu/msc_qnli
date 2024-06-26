bond_denomination_premise = 20
bond_denomination_hypothesis = 50

# the hypothesis talks about the bond denomination, which is also referenced in the premise
if bond_denomination_hypothesis < bond_denomination_premise:
    # check if the bond denomination in the hypothesis contradicts the bond denomination in the premise
    label = "contradiction"
else:
    # the premise and the hypothesis talk about different bond denominations, so we can't explicitly infer one from the other
    label = "neutral"

print(label)
