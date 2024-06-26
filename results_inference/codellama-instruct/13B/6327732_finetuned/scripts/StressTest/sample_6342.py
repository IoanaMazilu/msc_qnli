premise_amount = 288
hypothesis_amount = 588

# the hypothesis refers to the amount of money and the true discount
if hypothesis_amount <= premise_amount:
    # check if the hypothesis value contradicts the premise amount
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money
    # any amount of money greater than 'premise_amount' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
