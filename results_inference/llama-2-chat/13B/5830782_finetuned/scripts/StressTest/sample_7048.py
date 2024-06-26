percentage_below_cost_price_premise = 62
percentage_below_cost_price_hypothesis = 12

# the hypothesis talks about the percentage below cost price at which Vijay sells the cupboard, which is also referenced in the premise
if percentage_below_cost_price_hypothesis >= percentage_below_cost_price_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percentage_below_cost_price_premise'
    label = "contradiction"
elif percentage_below_cost_price_hypothesis < percentage_below_cost_price_premise:
    # the premise gives only an estimate for the percentage below cost price
    # any percentage below 'percentage_below_cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
