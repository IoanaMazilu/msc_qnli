pending_sales_increase_premise = 1.5
pending_sales_increase_hypothesis = 1.5

# the hypothesis and premise mention the percentage increase in pending sales in March
if pending_sales_increase_premise!= pending_sales_increase_hypothesis:
    # check if the percentage increase in pending sales in the hypothesis contradicts the percentage increase in the premise
    label = "contradiction"
else:
    # if the percentage increase in the hypothesis does not contradict the percentage increase in the premise, we can infer entailment
    label = "entailment"

print(label)
