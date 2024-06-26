store_z_premise = 90
store_z_hypothesis = 70
sales_tax_premise = 20
sales_tax_hypothesis = 20
rebate_premise = 10
rebate_hypothesis = 10

# the hypothesis refers to the total amount of money Isaac can spend at Store Z, including the sales tax and rebate
if store_z_premise <= store_z_hypothesis:
    # check if the estimate of'store_z_hypothesis' contradicts the total amount of money in the premise
    label = "contradiction"
elif sales_tax_hypothesis!= sales_tax_premise or rebate_hypothesis!= rebate_premise:
    # check if the sales tax or rebate in the hypothesis contradicts the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
