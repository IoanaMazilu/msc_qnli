store_z_price_premise = 50
store_z_price_hypothesis = 90
sales_tax_premise = 10
sales_tax_hypothesis = 10
rebate_premise = 10
rebate_hypothesis = 10

# the hypothesis refers to the price, sales tax, and rebate at Store Z mentioned in the premise
if store_z_price_hypothesis <= store_z_price_premise:
    # check if the price in the hypothesis contradicts the estimate of more than 'store_z_price_premise'
    label = "contradiction"
elif sales_tax_hypothesis != sales_tax_premise or rebate_hypothesis != rebate_premise:
    # check if the sales tax or rebate in the hypothesis contradicts the sales tax or rebate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the price at Store Z
    # a price greater than 'store_z_price_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
