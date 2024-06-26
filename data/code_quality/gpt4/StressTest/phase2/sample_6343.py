discount_premise = 588
discount_hypothesis = 288

# the hypothesis refers to the same discount mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the value of 'discount_hypothesis' contradicts the estimate of less than 'discount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any discount less than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
