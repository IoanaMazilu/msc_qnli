susan_weight_difference = 10
anna_weight = 10
total_weight = 110

# the hypothesis refers to the weight difference between Susan and Anna, which is also mentioned in the premise
if susan_weight_difference!= 40:
    # check if the weight difference in the hypothesis contradicts the weight difference in the premise
    label = "contradiction"
elif total_weight!= 110:
    # check if the total weight in the hypothesis contradicts the total weight in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
