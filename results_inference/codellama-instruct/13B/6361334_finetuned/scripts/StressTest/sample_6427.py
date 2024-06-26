sales_premise = 750
sales_hypothesis = 450

# the hypothesis refers to the number of items sold and the price mentioned in the premise
if sales_hypothesis >= sales_premise:
    # check if the hypothesis value contradicts the estimate of less than'sales_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of items sold
    # any number of items less than'sales_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
