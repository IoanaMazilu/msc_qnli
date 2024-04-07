# Premise: Store Z:$90, a 20% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Hypothesis: Store Z:$more than 70, a 20% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Golden Label: entailment

store_z_price_premise = 90
store_z_price_hypothesis = 70
sales_tax_premise = 0.20
sales_tax_hypothesis = 0.20
rebate_premise = 10
rebate_hypothesis = 10

# the hypothesis refers to the price at Store Z, sales tax, and rebate mentioned in the premise
if store_z_price_premise <= store_z_price_hypothesis:
    # check if the estimate of 'store_z_price_hypothesis' contradicts the price at Store Z in the premise
    label = "contradiction"
elif sales_tax_hypothesis != sales_tax_premise:
    # check if the sales tax in the hypothesis contradicts the sales tax reported in the premise
    label = "contradiction"
elif rebate_hypothesis != rebate_premise:
    # check if the rebate in the hypothesis contradicts the rebate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

