# Premise: Vijay sells a cupboard at 12% below cost price.
# Hypothesis: Vijay sells a cupboard at more than 12% below cost price.
# Golden Label: contradiction

below_cost_price_percentage_premise = 12
below_cost_price_percentage_hypothesis = 12

# the hypothesis talks about the percentage below cost price at which Vijay sells a cupboard, which is also mentioned in the premise
if below_cost_price_percentage_hypothesis <= below_cost_price_percentage_premise:
    # check if the hypothesis value contradicts the exact 'below_cost_price_percentage_premise'
    label = "contradiction"
elif below_cost_price_percentage_hypothesis > below_cost_price_percentage_premise:
    # check if the hypothesis value is greater than the 'below_cost_price_percentage_premise'
    # which would be consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

