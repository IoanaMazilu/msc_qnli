# Premise: Store Z:$80, a 20% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Hypothesis: Store Z:$less than 80, a 20% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Golden Label: contradiction

store_z_price_premise = 80
store_z_price_hypothesis = 80

# the hypothesis talks about the price of an item at Store Z, referenced also in the premise
if store_z_price_hypothesis >= store_z_price_premise:
    # check if the hypothesis value contradicts the price of 'store_z_price_premise'
    label = "contradiction"
else:
    # the premise gives the exact price at Store Z
    # any price less than 'store_z_price_premise' is not explicitly mentioned in the premise
    label = "neutral"

print(label)

