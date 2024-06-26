store_z_premise = 70
store_z_hypothesis = 90

# the hypothesis refers to the amount of money Isaac can spend at Store Z, which is also mentioned in the premise
if store_z_hypothesis <= store_z_premise:
    # check if the hypothesis value contradicts the estimate of more than'store_z_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money Isaac can spend
    # any amount of money greater than'store_z_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
