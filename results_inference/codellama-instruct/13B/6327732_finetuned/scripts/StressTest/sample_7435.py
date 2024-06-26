store_z_premise = 70
store_z_hypothesis = 90
sales_tax_premise = 20
sales_tax_hypothesis = 20
rebate_premise = 10
rebate_hypothesis = 10

# the hypothesis refers to the total cost of the item, which is the sum of the store Z cost, sales tax, and rebate
if store_z_hypothesis + sales_tax_hypothesis + rebate_hypothesis <= store_z_premise + sales_tax_premise + rebate_premise:
    # check if the hypothesis value contradicts the estimate of more than'store_z_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total cost of the item
    # any total cost greater than the premise estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
