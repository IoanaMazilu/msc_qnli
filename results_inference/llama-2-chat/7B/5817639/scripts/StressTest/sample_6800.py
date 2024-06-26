bond_purchase_premise = 4000
bond_purchase_hypothesis = 5000

# check if the hypothesis value contradicts the estimate of 'bond_purchase_premise'
if bond_purchase_hypothesis > bond_purchase_premise:
    label = "contradiction"
elif bond_purchase_hypothesis < bond_purchase_premise:
    # the hypothesis value is less than the premise estimate, so the hypothesis cannot be entailed from the premise
    label = "neutral"
else:
    # the hypothesis value is equal to the premise estimate, so entailment is possible
    label = "entailment"

print(label)
