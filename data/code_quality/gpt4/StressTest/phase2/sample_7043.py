weight_difference_premise = 10
weight_difference_hypothesis = 80
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis refers to the weight difference between Susan and Anna, and their total weight, both mentioned in the premise
if weight_difference_premise != weight_difference_hypothesis:
    # check if the weight difference in the hypothesis contradicts the weight difference in the premise
    label = "contradiction"
elif total_weight_premise != total_weight_hypothesis:
    # check if the total weight in the hypothesis contradicts the total weight in the premise
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the ones in the premise, we can infer neutrality
    label = "neutral"

print(label)
