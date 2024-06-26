discount_premise = 0.12
discount_hypothesis = 0.12

# the hypothesis talks about the discount Vijay gives for the cupboard, which is also referenced in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the estimate of more than 'discount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any discount greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
