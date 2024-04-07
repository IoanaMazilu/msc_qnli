# Premise: If bonds are sold in $50 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Hypothesis: If bonds are sold in $more than 20 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?
# Golden Label: entailment

bond_denomination_premise = [50, 100]
bond_denomination_hypothesis = [20, 100]

# the hypothesis and premise mention the possible denominations of bonds that Robert can purchase
if bond_denomination_premise != bond_denomination_hypothesis:
    # check if the denominations mentioned in the hypothesis contradict the denominations mentioned in the premise
    label = "contradiction"
else:
    # if the denominations in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)

