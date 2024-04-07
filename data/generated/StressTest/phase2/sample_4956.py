# Premise: Vijay sells a cupboard at 16% below cost price.
# Hypothesis: Vijay sells a cupboard at less than 86% below cost price.
# Golden Label: entailment

below_cost_price_premise = 16
below_cost_price_hypothesis = 86

# the hypothesis talks about the percentage below cost price at which Vijay sells a cupboard, as referenced in the premise
if below_cost_price_hypothesis < below_cost_price_premise:
    # check if the hypothesis value contradicts the premise value of 'below_cost_price_premise'
    label = "contradiction"
elif below_cost_price_hypothesis == below_cost_price_premise:
    # check if the hypothesis value is equivalent to the premise value
    label = "entailment"
else:
    # the premise gives the exact percentage below cost price
    # any percentage less than 'below_cost_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

