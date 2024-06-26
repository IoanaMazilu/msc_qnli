item_cost_premise = 70
item_cost_hypothesis = 90
tax_rate_premise = 20
tax_rate_hypothesis = 20
rebate_amount_premise = 10
rebate_amount_hypothesis = 10

# the hypothesis refers to the cost of the item, tax rate, and rebate amount in Store Z
if item_cost_hypothesis <= item_cost_premise:
    # check if the cost of the item in the hypothesis contradicts the premise
    label = "contradiction"
elif tax_rate_hypothesis!= tax_rate_premise or rebate_amount_hypothesis!= rebate_amount_premise:
    # check if the tax rate or rebate amount in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the cost of the item, tax rate, and rebate amount in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
