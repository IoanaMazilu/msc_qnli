price_premise = 28
price_hypothesis = 28

# the hypothesis talks about the price of crude oil, referenced also in the premise
if price_hypothesis <= price_premise:
    # check if the hypothesis value contradicts the estimate of the price in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the price, any price greater than 'price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
