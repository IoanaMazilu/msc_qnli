discount_premise = 25
discount_hypothesis = 85

# the hypothesis talks about the discount of the item, referenced also in the premise
if discount_premise >= discount_hypothesis:
    # check if the discount in the premise contradicts the estimate of less than 'discount_hypothesis'
    label = "contradiction"
else:
    # the premise gives a specific value for the discount
    # any discount less than 'discount_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
