susan_weight_premise = 40
susan_weight_hypothesis = 10
anna_weight_premise = 40
anna_weight_hypothesis = 40
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis refers to the weight of Susan and Anna, mentioned in the premise
if (susan_weight_hypothesis + anna_weight_hypothesis) <= (susan_weight_premise + anna_weight_premise):
    # check if the estimate of'susan_weight_hypothesis' and 'anna_weight_hypothesis' contradicts the weight of Susan and Anna in the premise
    label = "contradiction"
elif (susan_weight_hypothesis + anna_weight_hypothesis)!= total_weight_premise:
    # check if the total weight of Susan and Anna in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
