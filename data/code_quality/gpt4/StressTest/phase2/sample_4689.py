weight_difference_premise = 12
weight_difference_hypothesis = 62
total_weight_premise = 162
total_weight_hypothesis = 162

# the hypothesis refers to the weight difference between Susan and Anna and their total weight, both mentioned in the premise
if weight_difference_premise >= weight_difference_hypothesis:
    # check if the weight difference estimate in the hypothesis contradicts the weight difference in the premise
    label = "contradiction"
elif total_weight_premise != total_weight_hypothesis:
    # check if the total weight in the hypothesis contradicts the total weight in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
