discount_premise = 288
discount_hypothesis = 588

# the hypothesis talks about a discount on a sum, referenced also in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the estimate of less than 'discount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any discount greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
