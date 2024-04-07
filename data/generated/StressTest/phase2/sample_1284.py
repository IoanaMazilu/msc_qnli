# Premise: If bonds are sold in $50 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Hypothesis: If bonds are sold in $more than 10 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Golden Label: entailment

bond_denomination_premise = 50
bond_denomination_hypothesis = 10

# The hypothesis refers to the denomination of the bonds mentioned in the premise
if bond_denomination_hypothesis >= bond_denomination_premise:
    # Check if the 'bond_denomination_hypothesis' contradicts the denomination of the bonds in the premise
    label = "contradiction"
else:
    # If the hypothesis value doesn't contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

