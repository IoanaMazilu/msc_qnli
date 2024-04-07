# Premise: Susan weighs 20 pounds more than Anna does, and together they weigh a total of 160 pounds.
# Hypothesis: Susan weighs less than 80 pounds more than Anna does, and together they weigh a total of 160 pounds.
# Golden Label: entailment

weight_diff_premise = 20
weight_diff_hypothesis = 80
total_weight_premise = 160
total_weight_hypothesis = 160

# the hypothesis refers to the weight difference between Susan and Anna and the total weight, both mentioned in the premise
if weight_diff_hypothesis < weight_diff_premise:
    # check if the estimate of 'weight_diff_hypothesis' contradicts the weight difference in the premise
    label = "contradiction"
elif total_weight_hypothesis != total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
elif weight_diff_hypothesis == weight_diff_premise:
    # if the weight difference in the hypothesis exactly matches the weight difference in the premise, we can infer entailment
    label = "entailment"
else:
    # the hypothesis weight difference is larger than the premise, but does not contradict it, thus it is neutral
    label = "neutral"

print(label)

