store_cost_premise = 70
store_cost_hypothesis = 90
tax_rate_premise = 20
tax_rate_hypothesis = 20
rebate_premise = 10
rebate_hypothesis = 10

# the hypothesis refers to the cost of Store Z, tax rate, and rebate, which are also mentioned in the premise
if store_cost_premise!= store_cost_hypothesis:
    # check if the cost of Store Z in the hypothesis contradicts the cost of Store Z in the premise
    label = "contradiction"
elif tax_rate_premise!= tax_rate_hypothesis:
    # check if the tax rate in the hypothesis contradicts the tax rate in the premise
    label = "contradiction"
elif rebate_premise!= rebate_hypothesis:
    # check if the rebate in the hypothesis contradicts the rebate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
