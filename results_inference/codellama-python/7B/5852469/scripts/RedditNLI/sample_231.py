average_price_premise = 1200
average_price_hypothesis = 1200

# the hypothesis and premise mention the same average price
if average_price_hypothesis!= average_price_premise:
    # check if the average price in the hypothesis contradicts the average price in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average price
    # any estimate of the average price in the hypothesis greater or equal to 'average_price_premise' is consistent with the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
