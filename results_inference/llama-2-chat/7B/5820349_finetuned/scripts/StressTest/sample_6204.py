purchase_price_premise = 20
purchase_price_hypothesis = 60

# the hypothesis refers to the price of the items purchased, which is also mentioned in the premise
if purchase_price_premise >= purchase_price_hypothesis:
    # check if the estimate of 'purchase_price_hypothesis' contradicts the price of items in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
