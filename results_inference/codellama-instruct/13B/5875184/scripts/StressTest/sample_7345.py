premise_price_drop = 68
hypothesis_price_drop = 28

# the hypothesis refers to the price drop mentioned in the premise
if hypothesis_price_drop <= premise_price_drop:
    # check if the estimate of 'hypothesis_price_drop' contradicts the number of cookie sales in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
