premise_price = 70
hypothesis_price = 90

# the hypothesis talks about the price of the item
if hypothesis_price <= premise_price:
    # check if the price in the hypothesis contradicts the estimate of more than 'premise_price'
    label = "contradiction"
else:
    # the premise gives only an estimate for the price
    # any price greater than 'premise_price' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
