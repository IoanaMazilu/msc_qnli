pending_sales_premise = 1.5
pending_sales_hypothesis = 1.5

# the hypothesis and premise mention the percentage of pending sales of homes in the US
if pending_sales_hypothesis!= pending_sales_premise:
    # check if the percentage of pending sales in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage of pending sales in the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
