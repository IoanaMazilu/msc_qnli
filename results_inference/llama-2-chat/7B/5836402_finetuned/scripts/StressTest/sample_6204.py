purchase_price_premise = 20
purchase_price_hypothesis = 60

# the hypothesis refers to the purchase price of the items mentioned in the premise
if purchase_price_hypothesis <= purchase_price_premise:
    # check if the hypothesis value contradicts the estimate of more than 'purchase_price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the purchase price
    # any purchase price greater than 'purchase_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
