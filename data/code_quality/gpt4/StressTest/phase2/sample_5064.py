discount_premise = 14
discount_hypothesis = 84

# the hypothesis makes an assumption about the discount Vijay gives for selling the cupboard, also mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the discount given in the premise
    label = "contradiction"
else:
    # the premise gives a specific discount for the cupboard
    # any discount greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
