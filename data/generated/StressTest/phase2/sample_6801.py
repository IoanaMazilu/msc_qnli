# Premise: If bonds are sold in $50 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Hypothesis: If bonds are sold in $less than 70 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Golden Label: entailment

bond_denomination_premise = 50
bond_denomination_hypothesis = 70

# The hypothesis refers to the bond denominations mentioned in the premise
if bond_denomination_hypothesis > bond_denomination_premise:
    # The hypothesis value contradicts the premise value, as it suggests that bonds can be sold in denominations less than 70, which is higher than the premise value of 50
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise value, we cannot infer entailment or neutral, as the premise and hypothesis are asking a question and not providing a definite statement
    label = "neutral"

print(label)

