# define variables for the premise and hypothesis
premise_store_z = 70
premise_sales_tax = 20
premise_rebate_after_tax = 10
hypothesis_store_z = 90
hypothesis_sales_tax = 20
hypothesis_rebate_after_tax = 10

# compare the variables to determine the relation between the premise and hypothesis
if hypothesis_store_z <= premise_store_z:
    # check if the hypothesis value contradicts the estimate of 'premise_store_z'
    label = "contradiction"
elif hypothesis_sales_tax!= premise_sales_tax:
    # check if the hypothesis value contradicts the estimate of 'premise_sales_tax'
    label = "contradiction"
elif hypothesis_rebate_after_tax!= premise_rebate_after_tax:
    # check if the hypothesis value contradicts the estimate of 'premise_rebate_after_tax'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
