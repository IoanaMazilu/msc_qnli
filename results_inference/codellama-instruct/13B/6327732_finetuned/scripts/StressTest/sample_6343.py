premise_discount = 588
hypothesis_discount = 288

# the hypothesis refers to the discount on the same sum for the same time
if hypothesis_discount <= premise_discount:
    # check if the hypothesis value contradicts the estimate of less than 'premise_discount'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any discount greater than 'premise_discount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
