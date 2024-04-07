# Premise: Vijay sells a cupboard at less than 26% below cost price.
# Hypothesis: Vijay sells a cupboard at 16% below cost price.
# Golden Label: neutral

percentage_below_cost_price_premise = 26
percentage_below_cost_price_hypothesis = 16

# the hypothesis talks about the percentage below cost price that Vijay sells a cupboard, referenced also in the premise
if percentage_below_cost_price_hypothesis >= percentage_below_cost_price_premise:
    # check if the percentage below cost price in the hypothesis contradicts the estimate of less than 'percentage_below_cost_price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage below cost price
    # any percentage below cost price less than 'percentage_below_cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

