average_price_premise = 0
average_price_hypothesis = 0

# the hypothesis talks about the average price of t-shirts, referenced also in the premise
if average_price_hypothesis <= average_price_premise:
    # check if the hypothesis value contradicts the estimate of the average price in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average price
    # any average price greater than 'average_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
