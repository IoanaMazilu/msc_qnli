# Premise: Vijay sells a cupboard at less than 62% below cost price.
# Hypothesis: Vijay sells a cupboard at 12% below cost price.
# Golden Label: neutral

percent_below_cost_price_premise = 62
percent_below_cost_price_hypothesis = 12

# the hypothesis talks about the percentage below cost price at which Vijay sells a cupboard, referenced also in the premise
if percent_below_cost_price_hypothesis >= percent_below_cost_price_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percent_below_cost_price_premise'
    label = "contradiction"
else:
    # the premise gives only an upper limit for the percentage below cost price
    # any percentage below cost price less than 'percent_below_cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

