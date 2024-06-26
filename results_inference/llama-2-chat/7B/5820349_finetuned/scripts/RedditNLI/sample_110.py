pending_sales_rise_premise = 1.5
pending_sales_rise_hypothesis = 1.5

# the hypothesis and premise mention the percentage rise of pending sales of homes in March
if pending_sales_rise_premise!= pending_sales_rise_hypothesis:
    # check if the percentage rise in the hypothesis contradicts the percentage rise in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
