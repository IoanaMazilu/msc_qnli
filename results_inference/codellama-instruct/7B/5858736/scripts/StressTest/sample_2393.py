tshirt_price_premise = 8
tshirt_price_hypothesis = 8

# the hypothesis refers to the number of t-shirts and their average price mentioned in the premise
if tshirt_price_hypothesis >= tshirt_price_premise:
    # check if the estimate of 'tshirt_price_hypothesis' contradicts the number of t-shirts and their average price in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of t-shirts and their average price
    # any number of t-shirts and their average price less than 'tshirt_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
