prevailing_price_premise = 1000
prevailing_price_hypothesis = 1000

# the hypothesis talks about the prevailing price of a property with a smaller area than the premise
if prevailing_price_hypothesis <= prevailing_price_premise:
    # check if the hypothesis value contradicts the estimate of the prevailing price in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the prevailing price of a property with a larger area
    # any prevailing price of a property with a smaller area consistent with the premise is neutral, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
