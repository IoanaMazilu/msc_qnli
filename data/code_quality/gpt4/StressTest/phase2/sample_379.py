discount_premise = 50
discount_hypothesis = 20

# the hypothesis talks about the discount on the item's original price, which is also mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the hypothesis value contradicts the estimate of less than 'discount_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the discount
    # any discount less than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
