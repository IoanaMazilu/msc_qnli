price_premise = 20
price_hypothesis = 60

# the hypothesis talks about the number of items purchased, referenced also in the premise
if price_hypothesis <= price_premise:
    # check if the hypothesis value contradicts the estimate of more than 'price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of items purchased
    # any number of items greater than 'price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
