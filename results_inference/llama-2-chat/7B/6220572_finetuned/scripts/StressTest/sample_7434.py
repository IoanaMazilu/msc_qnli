store_z_premise = 90
store_z_hypothesis = 70
sales_tax_premise = 20
sales_tax_hypothesis = 20
rebate_after_tax_premise = 10
rebate_after_tax_hypothesis = 10

# the hypothesis refers to the value of'store_z','sales_tax', and'rebate_after_tax' mentioned in the premise
if store_z_hypothesis <= store_z_premise:
    # check if the hypothesis value contradicts the estimate of more than'store_z_premise'
    label = "contradiction"
elif sales_tax_hypothesis!= sales_tax_premise or rebate_after_tax_hypothesis!= rebate_after_tax_premise:
    # check if the sales tax or rebate after tax in the hypothesis contradicts the premise ones
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
