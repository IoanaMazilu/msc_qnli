premise_price = 70
hypothesis_price = 90

# the hypothesis refers to the price of the item and the tax and rebate mentioned in the premise
if hypothesis_price <= premise_price:
    # check if the estimate of 'hypothesis_price' contradicts the price mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the price
    # any price greater than 'premise_price' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
