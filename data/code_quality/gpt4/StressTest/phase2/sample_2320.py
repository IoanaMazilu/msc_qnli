total_sales_premise = 540
total_sales_hypothesis = 640

# the hypothesis refers to the total sales of corn and cotton mentioned in the premise
if total_sales_hypothesis <= total_sales_premise:
    # check if the total sales in the hypothesis contradicts the premise's 'more than total_sales_premise'
    label = "contradiction"
else:
    # the premise gives only a lower bound for the total sales
    # any total sales greater than 'total_sales_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
