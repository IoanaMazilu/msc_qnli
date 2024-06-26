pending_sales_premise = 1.5
pending_sales_hypothesis = 1.5

# check if the number in the hypothesis matches the number in the premise
if pending_sales_hypothesis == pending_sales_premise:
    # if the numbers match, we can infer entailment
    label = "entailment"
elif pending_sales_hypothesis > pending_sales_premise:
    # if the number in the hypothesis is greater than the number in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the numbers do not match, we cannot infer entailment or contradiction, so we get neutral
    label = "neutral"

print(label)
