bond_denominations_premise = [50, 100]
bond_denominations_hypothesis = [70, 100]

# the hypothesis mentions only two denominations, while the premise mentions three
if len(bond_denominations_hypothesis)!= len(bond_denominations_premise):
    # the hypothesis does not refer to all the denominations mentioned in the premise, so we cannot infer entailment or contradiction
    label = "neutral"
elif any(denom not in bond_denominations_premise for denom in bond_denominations_hypothesis):
    # the hypothesis mentions denominations not present in the premise, so we have a contradiction
    label = "contradiction"
else:
    # if the hypothesis mentions all the denominations present in the premise, we can infer entailment
    label = "entailment"

print(label)
