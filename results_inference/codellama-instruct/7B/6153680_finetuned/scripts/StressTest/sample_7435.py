store_z_premise = 70
store_z_hypothesis = 90
sales_tax_premise = 0.20
sales_tax_hypothesis = 0.20
rebate_premise = 10
rebate_hypothesis = 10

# the hypothesis refers to the same store, sales tax, and rebate as the premise
if store_z_hypothesis <= store_z_premise:
    # check if the store Z price in the hypothesis contradicts the premise
    label = "contradiction"
elif sales_tax_hypothesis!= sales_tax_premise:
    # check if the sales tax in the hypothesis contradicts the premise
    label = "contradiction"
elif rebate_hypothesis!= rebate_premise:
    # check if the rebate in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
