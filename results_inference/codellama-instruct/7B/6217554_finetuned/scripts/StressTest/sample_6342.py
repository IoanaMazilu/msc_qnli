discount_premise = 288
discount_hypothesis = 588

if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any number of discount greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
