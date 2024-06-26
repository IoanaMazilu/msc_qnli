price_premise = 28
price_hypothesis = 68

# the hypothesis refers to the percentage of price decrease mentioned in the premise
if price_hypothesis <= price_premise:
    # check if the hypothesis value contradicts the estimate of 'price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of price decrease
    # any percentage greater than 'price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
