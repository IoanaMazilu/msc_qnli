# Premise: Vijay sells a cupboard at 10% below cost price.
# Hypothesis: Vijay sells a cupboard at 40% below cost price.
# Golden Label: contradiction

below_cost_percent_premise = 10
below_cost_percent_hypothesis = 40

# the hypothesis talks about the percentage below cost price at which Vijay sells a cupboard, referenced also in the premise
if below_cost_percent_premise != below_cost_percent_hypothesis:
    # check if the percentage below cost price in the hypothesis contradicts the percentage below cost price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

