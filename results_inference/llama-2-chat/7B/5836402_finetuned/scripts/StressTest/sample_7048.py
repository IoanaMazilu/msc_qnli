discount_premise = 62
discount_hypothesis = 12

# the hypothesis talks about the discount of a cupboard, referenced also in the premise
if discount_hypothesis >= discount_premise:
    # check if the hypothesis value contradicts the estimate of less than 'discount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any discount less than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
