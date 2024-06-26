below_cost_price_premise = 86
below_cost_price_hypothesis = 16

# the hypothesis refers to the same percentage below cost price as in the premise
if below_cost_price_hypothesis >= below_cost_price_premise:
    # check if the percentage in the hypothesis contradicts the 'less than' estimate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage below cost price
    # any percentage below 'below_cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
