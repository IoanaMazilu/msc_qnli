items_purchased_premise = 20
items_purchased_hypothesis = 20

# the hypothesis refers to the number of items purchased mentioned in the premise
if items_purchased_hypothesis >= items_purchased_premise:
    # check if the estimate of 'items_purchased_hypothesis' contradicts the number of items purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
