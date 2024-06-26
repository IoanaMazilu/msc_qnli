premise_total = 90
premise_tax = 20
premise_rebate = 10

hypothesis_total = 70
hypothesis_tax = 20
hypothesis_rebate = 10

# check if the total cost in the hypothesis is greater than the total cost in the premise
if hypothesis_total > premise_total:
    # check if the sales tax in the hypothesis is the same as the sales tax in the premise
    if hypothesis_tax == premise_tax:
        # check if the rebate in the hypothesis is the same as the rebate in the premise
        if hypothesis_rebate == premise_rebate:
            # if all the conditions are met, we can infer entailment
            label = "entailment"
        else:
            # if the rebate in the hypothesis is different from the rebate in the premise, we can infer contradiction
            label = "contradiction"
    else:
        # if the sales tax in the hypothesis is different from the sales tax in the premise, we can infer contradiction
        label = "contradiction"
else:
    # if the total cost in the hypothesis is less than or equal to the total cost in the premise, we can infer neutral
    label = "neutral"

print(label)
