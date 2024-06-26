returned_tshirts_premise = 4
returned_tshirts_hypothesis = 8

# the hypothesis refers to the number of returned t-shirts and the average price of the remaining ones mentioned in the premise
if returned_tshirts_premise >= returned_tshirts_hypothesis:
    # check if the estimate of'returned_tshirts_hypothesis' contradicts the number of returned t-shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
