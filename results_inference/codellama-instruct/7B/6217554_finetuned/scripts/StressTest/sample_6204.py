items_purchased_premise = 20
items_purchased_hypothesis = 60

# the hypothesis gives an estimate for the number of items purchased
if items_purchased_hypothesis <= items_purchased_premise:
    # check if the estimate of 'items_purchased_hypothesis' contradicts the number of items purchased in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of items purchased
    # any number of items greater than 'items_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
