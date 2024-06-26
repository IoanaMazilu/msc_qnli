 price_discount_premise = 10
price_discount_hypothesis = 30

# the hypothesis talks about the discount on the listed price, which is also mentioned in the premise
if price_discount_hypothesis <= price_discount_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any discount greater than 'price_discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
