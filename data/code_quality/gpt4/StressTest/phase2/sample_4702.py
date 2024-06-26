percentage_below_cost_price_premise = 24
percentage_below_cost_price_hypothesis = 14

# the hypothesis refers to the percentage below cost price at which Vijay sells a cupboard
if percentage_below_cost_price_hypothesis >= percentage_below_cost_price_premise:
    # check if the percentage in the hypothesis contradicts the estimate of less than 'percentage_below_cost_price_premise'
    label = "contradiction"
elif percentage_below_cost_price_hypothesis < percentage_below_cost_price_premise:
    # the premise gives only an estimate for the percentage below cost price
    # any percentage below 'percentage_below_cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
