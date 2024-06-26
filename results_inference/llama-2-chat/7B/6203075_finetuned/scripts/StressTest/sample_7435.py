item_price_premise = 70
item_price_hypothesis = 90
sales_tax_premise = 20
sales_tax_hypothesis = 20
rebate_premise = 10
rebate_hypothesis = 10

# the hypothesis refers to the prices of the items, sales tax and rebate at store Z
if item_price_hypothesis <= item_price_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif sales_tax_hypothesis!= sales_tax_premise or rebate_hypothesis!= rebate_premise:
    # check if the sales tax or rebate at the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise and hypothesis values are the same, so we can infer entailment
    label = "entailment"

print(label)
