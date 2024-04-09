price_premise = 70
price_hypothesis = 90

# the hypothesis refers to the price of an item at Store Z mentioned in the premise
if price_hypothesis <= price_premise:
    # check if the hypothesis value contradicts the estimate of more than 'price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the price
    # any price greater than 'price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
