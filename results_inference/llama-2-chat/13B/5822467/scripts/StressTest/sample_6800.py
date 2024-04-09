bond_purchase_premise = 4000
bond_purchase_hypothesis = 5000

# the hypothesis refers to the amount of bonds purchased, mentioned in the premise
if bond_purchase_premise <= bond_purchase_hypothesis:
    # check if the estimate of 'bond_purchase_hypothesis' contradicts the amount of bonds purchased in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of bonds purchased
    # any amount of bonds greater than 'bond_purchase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
