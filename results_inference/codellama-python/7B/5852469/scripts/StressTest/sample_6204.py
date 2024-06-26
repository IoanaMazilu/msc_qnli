price_premise = 20
price_hypothesis = 60

# the hypothesis refers to the price of the items mentioned in the premise
if price_hypothesis <= price_premise:
    # check if the estimate of 'price_hypothesis' contradicts the price in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the price
    # any price greater than 'price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
