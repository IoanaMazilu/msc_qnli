premise_total = 90
premise_sales_tax = 0.20
premise_rebate = 10

hypothesis_total = 90
hypothesis_sales_tax = 0.20
hypothesis_rebate = 10

# the hypothesis refers to the total cost of the item, which is less than the total cost in the premise
if hypothesis_total < premise_total:
    # check if the estimate of 'hypothesis_total' contradicts the total cost in the premise
    label = "contradiction"
elif hypothesis_sales_tax!= premise_sales_tax:
    # check if the sales tax in the hypothesis contradicts the sales tax in the premise
    label = "contradiction"
elif hypothesis_rebate!= premise_rebate:
    # check if the rebate in the hypothesis contradicts the rebate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
