average_price_premise = 44
average_price_hypothesis = 54

# the hypothesis refers to the average price of the pieces of fruit mentioned in the premise
if average_price_hypothesis <= average_price_premise:
    # check if the estimate of 'average_price_hypothesis' contradicts the average price in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average price of fruit
    # any price less than 'average_price_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
