# Premise: Store Z:$70, a 30% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Hypothesis: Store Z:$more than 60, a 30% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Golden Label: entailment

store_z_price_premise = 70
store_z_price_hypothesis = 60
sales_tax_premise = 0.3
sales_tax_hypothesis = 0.3
rebate_premise = 10
rebate_hypothesis = 10

# the hypothesis refers to the price at Store Z, sales tax, and rebate mentioned in the premise
if store_z_price_hypothesis >= store_z_price_premise:
    # check if the estimate of 'store_z_price_hypothesis' contradicts the price at Store Z in the premise
    label = "contradiction"
elif sales_tax_hypothesis != sales_tax_premise or rebate_hypothesis != rebate_premise:
    # check if the sales tax and rebate in the hypothesis contradict the sales tax and rebate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

