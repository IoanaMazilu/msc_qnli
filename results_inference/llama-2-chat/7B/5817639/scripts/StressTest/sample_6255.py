discount_premise = 20
discount_hypothesis = 30

# the hypothesis refers to a discount percentage that is lower than the premise discount percentage
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the estimate of 'discount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount percentage
    # any discount percentage lower than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
