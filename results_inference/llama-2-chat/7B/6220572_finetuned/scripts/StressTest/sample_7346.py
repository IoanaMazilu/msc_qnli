price_change_premise = 28
price_change_hypothesis = 28

# the hypothesis talks about the price change of crude oil, referenced also in the premise
if price_change_hypothesis <= price_change_premise:
    # check if the hypothesis value contradicts the estimate of more than 'price_change_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the price change
    # any price change greater than 'price_change_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
