# Premise: Susan weighs 12 pounds more than Anna does, and together they weigh a total of 162 pounds.
# Hypothesis: Susan weighs 82 pounds more than Anna does, and together they weigh a total of 162 pounds.
# Golden Label: contradiction

susan_weight_more_premise = 12
susan_weight_more_hypothesis = 82
total_weight_premise = 162
total_weight_hypothesis = 162

# the hypothesis makes reference to the weight difference between Susan and Anna and their total weight, which were also reported in the premise
if susan_weight_more_hypothesis != susan_weight_more_premise:
    # check if the difference in weight between Susan and Anna stated in the hypothesis contradicts the one stated in the premise
    label = "contradiction"
elif total_weight_hypothesis != total_weight_premise:
    # check if the total weight of Susan and Anna stated in the hypothesis contradicts the one stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

