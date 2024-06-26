total_sales_premise = 100
total_sales_hypothesis = 200

# the hypothesis refers to the total sales of the company X & co mentioned in the premise
if total_sales_hypothesis <= total_sales_premise:
    # check if the estimate of 'total_sales_hypothesis' contradicts the number of total sales in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
