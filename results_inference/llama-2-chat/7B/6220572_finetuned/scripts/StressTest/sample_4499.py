discount_premise = 12
discount_hypothesis = 12

# the hypothesis refers to the discount on the cupboard mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the discount in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the discount
    # any discount greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
