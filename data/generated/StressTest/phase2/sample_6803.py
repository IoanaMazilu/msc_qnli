# Premise: If bonds are sold in $50 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Hypothesis: If bonds are sold in $10 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Golden Label: contradiction

bond_denomination_premise = [50, 100]
bond_denomination_hypothesis = [10, 100]

# The hypothesis refers to the bond denominations mentioned in the premise
if bond_denomination_hypothesis != bond_denomination_premise:
    # Check if the bond denominations in the hypothesis contradict the bond denominations mentioned in the premise
    label = "contradiction"
else:
    # If the bond denominations in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

