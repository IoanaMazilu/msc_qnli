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
