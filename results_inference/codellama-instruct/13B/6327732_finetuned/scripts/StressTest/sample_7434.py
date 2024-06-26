store_z_premise = 90
store_z_hypothesis = 70

# the hypothesis refers to the price of the item in store Z
if store_z_hypothesis <= store_z_premise:
    # check if the estimate of'store_z_hypothesis' contradicts the price of the item in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the price of the item in store Z
    # any price greater than'store_z_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
