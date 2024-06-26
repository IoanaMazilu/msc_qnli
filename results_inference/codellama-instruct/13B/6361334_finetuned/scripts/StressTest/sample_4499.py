cost_price_premise = 12
cost_price_hypothesis = 12

# the hypothesis refers to the percentage of discount mentioned in the premise
if cost_price_hypothesis <= cost_price_premise:
    # check if the estimate of 'cost_price_hypothesis' contradicts the percentage of discount in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of discount
    # any percentage of discount greater than 'cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
