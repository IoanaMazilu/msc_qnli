items_purchased_premise = 20
items_purchased_hypothesis = 60

# the hypothesis refers to the number of items purchased, mentioned in the premise
if items_purchased_premise >= items_purchased_hypothesis:
    # check if the number of items in the premise contradicts the estimate of 'items_purchased_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
