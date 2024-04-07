# Premise: Susan weighs 15 pounds more than Anna does, and together they weigh a total of 145 pounds.
# Hypothesis: Susan weighs 65 pounds more than Anna does, and together they weigh a total of 145 pounds.
# Golden Label: contradiction

weight_difference_premise = 15
weight_difference_hypothesis = 65
total_weight_premise = 145
total_weight_hypothesis = 145

# the hypothesis refers to the weight difference and total weight mentioned in the premise
if weight_difference_premise != weight_difference_hypothesis:
    # check if the weight difference in the hypothesis contradicts the weight difference reported in the premise
    label = "contradiction"
elif total_weight_hypothesis != total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "contradiction"

print(label)

