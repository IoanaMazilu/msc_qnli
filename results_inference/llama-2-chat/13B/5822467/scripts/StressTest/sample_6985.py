pen_sales_premise = 42.00
pen_sales_hypothesis = 12.00

# the hypothesis refers to the number of pens purchased and the total amount spent
if pen_sales_hypothesis <= pen_sales_premise:
    # check if the estimate of 'pen_sales_hypothesis' contradicts the amount spent in the premise
    label = "contradiction"
elif pen_sales_premise!= pen_sales_hypothesis:
    # check if the number of pens purchased in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
