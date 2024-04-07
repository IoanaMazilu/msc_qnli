# Premise: Vijay sells a cupboard at less than 22% below cost price.
# Hypothesis: Vijay sells a cupboard at 12% below cost price.
# Golden Label: neutral

below_cost_price_percentage_premise = 22
below_cost_price_percentage_hypothesis = 12

# the hypothesis talks about the percentage below cost price at which Vijay sells a cupboard, which is also referenced in the premise
if below_cost_price_percentage_hypothesis >= below_cost_price_percentage_premise:
    # check if the hypothesis value contradicts the estimate of less than 'below_cost_price_percentage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage below cost price
    # any percentage below 'below_cost_price_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

