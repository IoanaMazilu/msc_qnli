price_premise = 28
price_hypothesis = 5

# the hypothesis refers to the price of crude oil and the premise mentions a decrease in the price
if price_hypothesis <= price_premise:
    # check if the hypothesis value contradicts the estimate of more than 'price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the price
    # any price increase greater than 'price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
