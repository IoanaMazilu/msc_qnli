store_z_premise = 70
store_z_hypothesis = 90

# the hypothesis refers to the price of Store Z mentioned in the premise
if store_z_hypothesis <= store_z_premise:
    # check if the hypothesis value contradicts the estimate of'store_z_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the price of Store Z
    # any price greater than'store_z_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
