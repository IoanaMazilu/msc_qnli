bond_purchase_premise = 4000
bond_purchase_hypothesis = 5000

# the hypothesis refers to the total amount of US saving bonds purchased by Robert
if bond_purchase_hypothesis <= bond_purchase_premise:
    # check if the estimate of 'bond_purchase_hypothesis' contradicts the total amount of bonds purchased in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total amount of US saving bonds purchased
    # any amount greater than 'bond_purchase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
