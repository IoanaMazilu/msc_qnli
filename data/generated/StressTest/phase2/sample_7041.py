# Premise: Susan weighs 10 pounds more than Anna does, and together they weigh a total of 110 pounds.
# Hypothesis: Susan weighs less than 40 pounds more than Anna does, and together they weigh a total of 110 pounds.
# Golden Label: entailment

susan_weight_difference_premise = 10
susan_weight_difference_hypothesis = 40
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis refers to the weight difference between Susan and Anna, and their total weight mentioned in the premise
if susan_weight_difference_hypothesis < susan_weight_difference_premise:
    # check if the estimate of 'susan_weight_difference_hypothesis' contradicts the weight difference in the premise
    label = "contradiction"
elif total_weight_hypothesis != total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

