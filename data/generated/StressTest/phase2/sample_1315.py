# Premise: Store Z:$more than 60, a 20% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Hypothesis: Store Z:$90, a 20% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Golden Label: neutral

store_z_price_premise = 60
store_z_price_hypothesis = 90

# the hypothesis refers to the price of an item at Store Z mentioned in the premise
if store_z_price_hypothesis <= store_z_price_premise:
    # check if the price of the item at Store Z in the hypothesis contradicts the estimate of more than 'store_z_price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the price of the item at Store Z
    # any price greater than 'store_z_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

