store_z_price_premise = 70
store_z_price_hypothesis = 90

# the hypothesis refers to the price of an item in Store Z, also mentioned in the premise
if store_z_price_hypothesis <= store_z_price_premise:
    # check if the hypothesis price contradicts the estimate of more than'store_z_price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the price of the item
    # any price greater than'store_z_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
