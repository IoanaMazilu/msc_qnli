# Premise: If bonds are sold in $50 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Hypothesis: If bonds are sold in $70 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Golden Label: contradiction

bond_denomination_premise = [50, 100]
bond_denomination_hypothesis = [70, 100]

# both premise and hypothesis refer to the possible denominations of the bonds that Robert purchased
if bond_denomination_premise != bond_denomination_hypothesis:
    # the premise and hypothesis provide different possible denominations for the bonds
    # since the denominations do not match, we cannot make a clear inference
    label = "neutral"

print(label)

