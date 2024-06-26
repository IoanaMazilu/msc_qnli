store_z_premise = 80
store_z_hypothesis = 50
sales_tax_premise = sales_tax_hypothesis = 0.20
rebate_premise = rebate_hypothesis = 10

# the hypothesis refers to the cost at Store Z, the sales tax and the rebate after tax mentioned in the premise
if store_z_hypothesis >= store_z_premise:
    # check if the estimate of 'store_z_hypothesis' contradicts the cost at Store Z in the premise
    label = "contradiction"
elif sales_tax_hypothesis != sales_tax_premise or rebate_hypothesis != rebate_premise:
    # check if the sales tax or the rebate after tax in the hypothesis contradicts the values reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
