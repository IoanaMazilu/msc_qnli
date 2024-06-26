susan_weight_difference_premise = 10
anna_weight_difference_premise = 10
total_weight_premise = 110
susan_weight_difference_hypothesis = 80
anna_weight_difference_hypothesis = 10
total_weight_hypothesis = 110

# the hypothesis refers to the weight difference between Susan and Anna, which is also mentioned in the premise
if susan_weight_difference_hypothesis!= susan_weight_difference_premise:
    # check if the weight difference between Susan and Anna in the hypothesis contradicts the weight difference in the premise
    label = "contradiction"
elif anna_weight_difference_hypothesis!= anna_weight_difference_premise:
    # check if the weight difference between Anna and Susan in the hypothesis contradicts the weight difference in the premise
    label = "contradiction"
elif total_weight_hypothesis!= total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
