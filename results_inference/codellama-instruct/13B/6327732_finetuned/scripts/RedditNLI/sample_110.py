pending_sales_premise = 1.5
pending_sales_hypothesis = 1.5

# the hypothesis and premise mention the same percentage of pending sales in March
if pending_sales_premise!= pending_sales_hypothesis:
    # check if the percentage of pending sales in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage of pending sales in the hypothesis is consistent with the premise, we can infer entailment
    label = "entailment"

print(label)
