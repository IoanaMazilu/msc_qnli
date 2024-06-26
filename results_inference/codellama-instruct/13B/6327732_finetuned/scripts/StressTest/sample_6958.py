toys_purchased_premise = 20
toys_purchased_hypothesis = 375

# the hypothesis refers to the rate at which toys were purchased, which is not mentioned in the premise
if toys_purchased_hypothesis <= toys_purchased_premise:
    # check if the estimate of 'toys_purchased_hypothesis' contradicts the number of toys purchased in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of toys purchased
    # any number of toys greater than 'toys_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
