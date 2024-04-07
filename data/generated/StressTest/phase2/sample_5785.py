# Premise: Vijay sells a cupboard at less than 60% below cost price.
# Hypothesis: Vijay sells a cupboard at 10% below cost price.
# Golden Label: neutral

below_cost_price_premise = 60
below_cost_price_hypothesis = 10

# the hypothesis refers to the same sale as the premise, but with a different percentage below the cost price
if below_cost_price_hypothesis >= below_cost_price_premise:
    # check if the percentage below the cost price in the hypothesis contradicts the premise that it's less than 'below_cost_price_premise'
    label = "contradiction"
else:
    # any percentage below the cost price less than 'below_cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

