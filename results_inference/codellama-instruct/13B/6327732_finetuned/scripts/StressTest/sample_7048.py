cost_price_premise = 100
cost_price_hypothesis = 100

# the hypothesis refers to the percentage of discount applied to the cost price
if cost_price_hypothesis <= cost_price_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cost_price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of discount
    # any percentage of discount greater than 'cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
