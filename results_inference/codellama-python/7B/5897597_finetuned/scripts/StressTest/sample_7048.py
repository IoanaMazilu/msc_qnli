below_cost_price_premise = 62
below_cost_price_hypothesis = 12

# the hypothesis talks about the percentage below cost price at which Vijay sells a cupboard, referenced also in the premise
if below_cost_price_hypothesis >= below_cost_price_premise:
    # check if the hypothesis value contradicts the estimate of less than 'below_cost_price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage below cost price
    # any percentage below 'below_cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
