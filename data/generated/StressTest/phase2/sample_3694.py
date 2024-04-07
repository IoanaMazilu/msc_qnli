# Premise: If bonds are sold in $more than 40 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Hypothesis: If bonds are sold in $50 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Golden Label: neutral

bond_denomination_premise = 40
bond_denomination_hypothesis = 50

# the hypothesis talks about the denomination of bonds, which is also discussed in the premise
if bond_denomination_hypothesis <= bond_denomination_premise:
    # check if the hypothesis bond denomination contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the bond denomination
    # any bond denomination greater than 'bond_denomination_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

