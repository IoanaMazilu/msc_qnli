# Premise: If Lary received $800 more than Terry did, what was the profit made by their business in that year?
# Hypothesis: If Lary received $500 more than Terry did, what was the profit made by their business in that year?
# Golden Label: contradiction

lary_extra_premise = 800
lary_extra_hypothesis = 500

# the hypothesis refers to the difference in the amount received by Lary and Terry compared to the premise
if lary_extra_hypothesis != lary_extra_premise:
    # check if the difference in the hypothesis contradicts the difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

