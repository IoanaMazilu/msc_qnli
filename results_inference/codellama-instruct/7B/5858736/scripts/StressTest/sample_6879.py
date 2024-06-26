# define variables with representative names for the numerical entities in both inputs
bond_purchase_premise = 1500
bond_purchase_hypothesis = 6500

# extract all quantities as valid numbers (integers or floats)
bond_purchase_premise = float(bond_purchase_premise)
bond_purchase_hypothesis = float(bond_purchase_hypothesis)

# use brief comments to explain what comparison you do between the defined variables
if bond_purchase_hypothesis <= bond_purchase_premise:
    # check if the hypothesis value contradicts the estimate of 'bond_purchase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of bonds purchased
    # any amount greater than 'bond_purchase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
