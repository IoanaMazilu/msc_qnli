store_z_premise = 70
store_z_hypothesis = 90
sales_tax_premise = 20
sales_tax_hypothesis = 20
rebate_premise = 10
rebate_hypothesis = 10

# the hypothesis refers to the price of the item and the sales tax and rebate mentioned in the premise
if store_z_hypothesis <= store_z_premise:
    # check if the estimate of'store_z_hypothesis' contradicts the number of cookie sales in the premise
    label = "contradiction"
elif sales_tax_hypothesis!= sales_tax_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
elif rebate_hypothesis!= rebate_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
