cost_price_premise = 62
cost_price_hypothesis = 12

# the hypothesis talks about the selling price of the cupboard, referenced also in the premise
if cost_price_hypothesis >= cost_price_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cost_price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the selling price
    # any selling price less than 'cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
