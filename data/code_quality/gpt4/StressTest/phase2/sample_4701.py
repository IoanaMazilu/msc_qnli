discount_premise = 14
discount_hypothesis = 24

# the hypothesis refers to the discount at which the cupboard is sold, also mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives a specific discount value
    # any discount greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
