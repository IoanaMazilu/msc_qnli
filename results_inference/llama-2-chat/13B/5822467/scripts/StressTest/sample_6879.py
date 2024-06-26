bond_purchase_premise = 1500
bond_purchase_hypothesis = 6500

# the hypothesis refers to the amount of bonds purchased
if bond_purchase_hypothesis < bond_purchase_premise:
    # the hypothesis value is less than the premise value, so there is no contradiction
    label = "neutral"
elif bond_purchase_hypothesis > bond_purchase_premise:
    # the hypothesis value is greater than the premise value, so there is entailment
    label = "entailment"
else:
    # the hypothesis value is equal to the premise value, so there is no contradiction or entailment
    label = "neutral"

print(label)
