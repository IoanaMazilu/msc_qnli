cost_price_premise = 120
cost_price_hypothesis = 108

# the hypothesis talks about the discount on the cost price, which is also mentioned in the premise
if cost_price_hypothesis <= cost_price_premise:
    # check if the hypothesis value contradicts the estimate of more than 'cost_price_premise' discount
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount,
    # any discount greater than 'cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
