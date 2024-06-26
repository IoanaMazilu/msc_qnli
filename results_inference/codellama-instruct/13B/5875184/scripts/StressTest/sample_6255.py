premise_discount = 20
hypothesis_discount = 30

# the hypothesis refers to the discount percentage mentioned in the premise
if hypothesis_discount >= premise_discount:
    # check if the hypothesis value contradicts the estimate of less than 'premise_discount'
    label = "contradiction"
else:
    # the premise gives an estimate for the discount percentage
    # any discount percentage less than 'premise_discount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
