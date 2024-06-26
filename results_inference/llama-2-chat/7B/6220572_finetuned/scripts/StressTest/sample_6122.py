tshirts_returned_premise = 4
tshirts_returned_hypothesis = 8
average_price_remaining_premise = 0
average_price_remaining_hypothesis = 0

# the hypothesis refers to the number of returned t-shirts and the average price of the remaining t-shirts mentioned in the premise
if tshirts_returned_hypothesis!= tshirts_returned_premise:
    # check if the number of returned t-shirts in the hypothesis contradicts the number of returned t-shirts reported in the premise
    label = "contradiction"
elif average_price_remaining_hypothesis!= average_price_remaining_premise:
    # check if the average price of the remaining t-shirts in the hypothesis contradicts the average price of the remaining t-shirts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
