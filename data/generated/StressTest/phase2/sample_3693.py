# Premise: If bonds are sold in $50 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Hypothesis: If bonds are sold in $more than 40 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Golden Label: entailment

bond_denomination_premise = 50
bond_denomination_hypothesis = 40

# the hypothesis suggests a bond denomination lower than the premise
if bond_denomination_hypothesis >= bond_denomination_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)

