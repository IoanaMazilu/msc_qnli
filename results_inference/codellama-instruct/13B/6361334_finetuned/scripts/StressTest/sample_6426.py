sales_premise = 450
sales_hypothesis = 750

# the hypothesis refers to the number of sold items and their price, mentioned in the premise
if sales_hypothesis >= sales_premise:
    # check if the estimate of'sales_hypothesis' contradicts the number of sold items in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of sold items
    # any number of sold items less than'sales_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
