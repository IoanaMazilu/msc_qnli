discount_premise = 588
discount_hypothesis = 588

# the hypothesis refers to the discount value mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the estimate of 'discount_hypothesis' contradicts the discount value in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount value
    # any discount value greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
