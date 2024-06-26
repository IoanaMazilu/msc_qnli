bond_purchase_premise = 4000
bond_purchase_hypothesis = 5000

if bond_purchase_hypothesis <= bond_purchase_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
