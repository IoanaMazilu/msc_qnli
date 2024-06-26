susan_weight_premise = 10
anna_weight_premise = 10
total_weight_premise = 110
susan_weight_hypothesis = 40
anna_weight_hypothesis = 10
total_weight_hypothesis = 110

# the hypothesis refers to the weight difference between Susan and Anna, and the total weight of both, mentioned in the premise
if susan_weight_premise >= susan_weight_hypothesis:
    # check if the estimate of'susan_weight_hypothesis' contradicts the weight difference in the premise
    label = "contradiction"
elif anna_weight_hypothesis!= anna_weight_premise:
    # check if the weight of Anna in the hypothesis contradicts the weight of Anna reported in the premise
    label = "contradiction"
elif total_weight_hypothesis!= total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
