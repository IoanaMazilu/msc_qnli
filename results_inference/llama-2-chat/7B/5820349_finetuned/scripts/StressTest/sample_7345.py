price_change_premise = 68
price_change_hypothesis = 28

# the hypothesis refers to the price change of crude oil mentioned in the premise
if price_change_hypothesis >= price_change_premise:
    # check if the estimate of 'price_change_hypothesis' contradicts the price change in the premise
    label = "contradiction"
elif price_change_hypothesis < price_change_premise:
    # the premise gives an estimate for the price change
    # any price change less than 'price_change_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
