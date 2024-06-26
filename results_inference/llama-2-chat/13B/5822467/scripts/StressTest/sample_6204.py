ram_price_premise = 20
ram_price_hypothesis = 60

# the hypothesis refers to the price of the items purchased from Ram
if ram_price_hypothesis <= ram_price_premise:
    # check if the hypothesis value contradicts the estimate of 'ram_price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the price of the items
    # any price less than 'ram_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
