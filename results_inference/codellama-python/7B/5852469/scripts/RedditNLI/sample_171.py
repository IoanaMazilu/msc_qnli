price_premise = 2.5
price_hypothesis = 2.5

# the hypothesis and premise mention the average price of a gallon of gasoline in the US
if price_hypothesis!= price_premise:
    # check if the average price in the hypothesis contradicts the average price in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average price
    # any estimate of the average price in the hypothesis greater or equal to 'price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
