discount_premise = 20
discount_hypothesis = 30

# the hypothesis refers to the discount percentage Jeevan got, which is also mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the discount percentage mentioned in the hypothesis contradicts the premise estimate of more than 'discount_premise'
    label = "contradiction"
else:
    # the premise only gives an estimate for the discount percentage
    # any discount percentage greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
