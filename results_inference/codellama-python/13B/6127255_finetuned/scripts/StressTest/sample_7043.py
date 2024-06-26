weight_difference_premise = 10
weight_difference_hypothesis = 80
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis refers to the weight difference between Susan and Anna and their total weight, both mentioned in the premise
if weight_difference_hypothesis!= weight_difference_premise:
    # check if the weight difference in the hypothesis contradicts the weight difference reported in the premise
    label = "contradiction"
elif total_weight_hypothesis!= total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
