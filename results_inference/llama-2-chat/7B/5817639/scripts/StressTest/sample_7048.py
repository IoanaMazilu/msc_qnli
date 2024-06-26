cost_price_premise = 62
cost_price_hypothesis = 12

# the hypothesis talks about the cost price of a cupboard, referenced also in the premise
if cost_price_hypothesis <= cost_price_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cost_price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the cost price
    # any cost price greater than 'cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
