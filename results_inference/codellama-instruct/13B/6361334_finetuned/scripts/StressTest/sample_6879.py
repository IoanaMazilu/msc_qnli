bond_purchase_premise = 1500
bond_purchase_hypothesis = 6500

# the hypothesis refers to the amount of US saving bonds purchased by Robert
if bond_purchase_hypothesis >= bond_purchase_premise:
    # check if the estimate of 'bond_purchase_hypothesis' contradicts the amount of bonds purchased in the premise
    label = "contradiction"
else:
    # the premise gives an exact amount for the amount of bonds purchased
    # any amount of bonds less than 'bond_purchase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
