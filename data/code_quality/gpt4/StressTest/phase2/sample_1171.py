price_premise = 50
price_hypothesis = 80
sales_tax_premise = 20
sales_tax_hypothesis = 20
rebate_premise = 10
rebate_hypothesis = 10

# the hypothesis refers to the price, sales tax and rebate mentioned in the premise
if price_hypothesis <= price_premise:
    # check if the price in the hypothesis contradicts the estimate of more than 'price_premise'
    label = "contradiction"
elif sales_tax_hypothesis != sales_tax_premise:
    # check if the sales tax in the hypothesis contradicts the sales tax reported in the premise
    label = "contradiction"
elif rebate_hypothesis != rebate_premise:
    # check if the rebate in the hypothesis contradicts the rebate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the price
    # any price greater than 'price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
