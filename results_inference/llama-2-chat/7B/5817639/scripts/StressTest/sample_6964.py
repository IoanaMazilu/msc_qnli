prevailing_price_premise = 1000
prevailing_price_hypothesis = 1000

# the hypothesis talks about the price of a 700 square feet property, which is also referred to in the premise
if prevailing_price_hypothesis <= prevailing_price_premise:
    # check if the hypothesis value contradicts the estimate of the prevailing price in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the price of a property, and any price consistent with that estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
