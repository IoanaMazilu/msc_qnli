average_price_premise = 75
average_price_hypothesis = 45

# the hypothesis refers to the average price of the fruit mentioned in the premise
if average_price_hypothesis >= average_price_premise:
    # check if the 'average_price_hypothesis' contradicts the premise of less than 'average_price_premise'
    label = "contradiction"
else:
    # the premise gives only a boundary for the average price
    # any average price less than 'average_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
