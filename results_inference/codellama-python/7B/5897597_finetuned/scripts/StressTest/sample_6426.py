sales_premise = 450
sales_hypothesis = 750

# the hypothesis refers to the amount of money George got from selling something, which is also mentioned in the premise
if sales_premise >= sales_hypothesis:
    # check if the amount of sales in the premise contradicts the estimate of less than'sales_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
