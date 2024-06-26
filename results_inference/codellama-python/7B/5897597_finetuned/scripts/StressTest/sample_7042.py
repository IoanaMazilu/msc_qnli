weight_difference_premise = 40
weight_difference_hypothesis = 10
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis refers to the weight difference between Susan and Anna and their total weight, mentioned in the premise
if weight_difference_hypothesis > weight_difference_premise:
    # check if the weight difference in the hypothesis contradicts the weight difference in the premise
    label = "contradiction"
elif total_weight_hypothesis!= total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight difference
    # any weight difference less than 'weight_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
