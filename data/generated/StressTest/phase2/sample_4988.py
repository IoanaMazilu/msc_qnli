# Premise: Susan weighs 20 pounds more than Anna does, and together they weigh a total of 160 pounds.
# Hypothesis: Susan weighs less than 20 pounds more than Anna does, and together they weigh a total of 160 pounds.
# Golden Label: contradiction

weight_difference_premise = 20
weight_difference_hypothesis = 20
total_weight_premise = 160
total_weight_hypothesis = 160

# the hypothesis refers to weight difference and total weight mentioned in the premise
if weight_difference_hypothesis >= weight_difference_premise:
    # check if the estimate of 'weight_difference_hypothesis' contradicts the weight difference in the premise
    label = "contradiction"
elif total_weight_hypothesis != total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

