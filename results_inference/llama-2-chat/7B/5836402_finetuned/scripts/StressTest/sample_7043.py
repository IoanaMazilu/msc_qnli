susan_weight_premise = 10
susan_weight_hypothesis = 80
anna_weight_premise = 10
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis refers to the weight of Susan and Anna mentioned in the premise
if susan_weight_premise!= susan_weight_hypothesis:
    # check if the weight of Susan in the hypothesis contradicts the weight in the premise
    label = "contradiction"
elif anna_weight_premise!= anna_weight_hypothesis:
    # check if the weight of Anna in the hypothesis contradicts the weight in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
