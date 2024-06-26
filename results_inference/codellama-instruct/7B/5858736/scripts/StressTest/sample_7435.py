premise_total = 70
premise_tax = 0.20
premise_rebate = 10

hypothesis_total = 90
hypothesis_tax = 0.20
hypothesis_rebate = 10

# check if the total cost in the hypothesis contradicts the total cost reported in the premise
if hypothesis_total <= premise_total:
    label = "contradiction"
# check if the sales tax in the hypothesis contradicts the sales tax reported in the premise
elif hypothesis_tax!= premise_tax:
    label = "contradiction"
# check if the rebate in the hypothesis contradicts the rebate reported in the premise
elif hypothesis_rebate!= premise_rebate:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
