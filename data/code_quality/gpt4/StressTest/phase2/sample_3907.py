average_price_premise = 40
average_price_hypothesis = 50

# both the hypothesis and premise refer to an average price of fruit that Mary keeps
if average_price_hypothesis <= average_price_premise:
    # if the average price in the hypothesis contradicts the premise (is less or equal)
    label = "contradiction"
else:
    # the premise gives only an estimate for the average price
    # any average price greater than 'average_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
