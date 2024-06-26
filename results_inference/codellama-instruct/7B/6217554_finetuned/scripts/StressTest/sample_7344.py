price_crude_premise = 28
price_crude_hypothesis = 68

# the hypothesis talks about the price of crude oil, referenced also in the premise
if price_crude_hypothesis >= price_crude_premise:
    # check if the estimate of 'price_crude_hypothesis' contradicts the percentage decrease in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage decrease in the price of crude
    # any percentage decrease less than 'price_crude_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
