bond_purchase_premise = 1500
bond_purchase_hypothesis = 7500

# the hypothesis refers to the amount of US saving bonds purchased
if bond_purchase_hypothesis > bond_purchase_premise:
    # the hypothesis value is greater than the premise value, entailment can be inferred
    label = "entailment"
elif bond_purchase_hypothesis == bond_purchase_premise:
    # the hypothesis value is equal to the premise value, no contradiction or entailment can be inferred
    label = "neutral"
else:
    # the hypothesis value is less than the premise value, contradiction can be inferred
    label = "contradiction"

print(label)
