store_z_premise = 90
store_z_hypothesis = 90
sales_tax_premise = 20
sales_tax_hypothesis = 20
rebate_premise = 10
rebate_hypothesis = 10

# the hypothesis refers to the total amount of money Isaac can spend at Store Z, including the sales tax and rebate
if store_z_hypothesis >= store_z_premise:
    # check if the hypothesis value contradicts the premise estimate of less than'store_z_premise'
    label = "contradiction"
elif sales_tax_hypothesis!= sales_tax_premise or rebate_hypothesis!= rebate_premise:
    # check if the sales tax or rebate in the hypothesis contradicts the ones in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total amount of money Isaac can spend
    # any amount less than'store_z_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
