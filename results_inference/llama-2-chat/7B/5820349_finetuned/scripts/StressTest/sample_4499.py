below_cost_price_premise = 12
below_cost_price_hypothesis = 12

# the hypothesis refers to the percentage below cost price at which Vijay sells a cupboard, mentioned in the premise
if below_cost_price_hypothesis <= below_cost_price_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
