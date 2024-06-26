premise_price_drop = 28
hypothesis_price_drop = 68

# the hypothesis refers to the price drop mentioned in the premise
if hypothesis_price_drop <= premise_price_drop:
    # check if the estimate of 'hypothesis_price_drop' contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the price drop
    # any price drop greater than 'premise_price_drop' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
