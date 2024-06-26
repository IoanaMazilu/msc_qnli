average_price_premise = 50
average_price_hypothesis = 40

# the hypothesis talks about the average price of the pieces of fruit that Mary keeps, which is also mentioned in the premise
if average_price_hypothesis!= average_price_premise:
    # check if the average price in the hypothesis contradicts the average price mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average price of the pieces of fruit
    # any average price that is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
