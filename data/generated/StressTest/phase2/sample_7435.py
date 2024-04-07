# Premise: Store Z:$more than 70, a 20% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Hypothesis: Store Z:$90, a 20% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Golden Label: neutral

store_z_price_premise = 70
store_z_price_hypothesis = 90
sales_tax_rate = 0.20
rebate = 10

# the hypothesis talks about the price in Store Z which is also mentioned in the premise
if store_z_price_hypothesis <= store_z_price_premise:
    # check if the hypothesis value contradicts the estimate of 'more than' store_z_price_premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the price in Store Z
    # any price greater than store_z_price_premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

