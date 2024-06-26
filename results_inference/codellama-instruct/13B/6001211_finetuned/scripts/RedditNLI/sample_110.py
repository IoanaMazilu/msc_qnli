pending_sales_rose_premise = 1.5
pending_sales_rose_hypothesis = 1.5

# the hypothesis and premise mention the percentage of pending sales of homes that rose in March
if pending_sales_rose_hypothesis!= pending_sales_rose_premise:
    # check if the percentage of pending sales that rose in the hypothesis contradicts the percentage that rose in the premise
    label = "contradiction"
else:
    # if the percentage of pending sales that rose in the hypothesis does not contradict the percentage that rose in the premise, we can infer entailment
    label = "entailment"

print(label)
