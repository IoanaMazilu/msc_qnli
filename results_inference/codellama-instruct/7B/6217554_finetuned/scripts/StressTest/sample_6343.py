discount_premise = 588
discount_hypothesis = 288

if discount_hypothesis >= discount_premise:
    # check if the discount in the hypothesis contradicts the estimate of less than 'discount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any discount less than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
