# Premise: Karin's science class weighed plastic rings for an experiment and they found that the orange ring weighed 0.08333333333333333 ounce, the purple ring weighed 0.3333333333333333 ounce, and the white ring weighed 0.4166666666666667 ounce.
# Hypothesis: The total weight of the plastic rings is 2.5.
# Golden Label: contradiction

orange_ring_weight_premise = 0.08333333333333333
purple_ring_weight_premise = 0.3333333333333333
white_ring_weight_premise = 0.4166666666666667
total_weight_hypothesis = 2.5

# the hypothesis refers to the total weight of the rings, which are also mentioned in the premise
# compute the total weight of the rings in the premise
total_weight_premise = orange_ring_weight_premise + purple_ring_weight_premise + white_ring_weight_premise
if total_weight_hypothesis != total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

