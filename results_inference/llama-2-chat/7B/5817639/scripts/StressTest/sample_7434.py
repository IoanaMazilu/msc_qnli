store_z_premise = 90
store_z_hypothesis = 70

# the hypothesis refers to the amount of money available for purchasing an item, as shown in the table
if store_z_hypothesis <= store_z_premise:
    # check if the hypothesis value contradicts the estimate of'store_z_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money available for purchasing an item
    # any amount of money greater than'store_z_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
