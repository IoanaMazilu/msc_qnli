susan_weight_premise = 10
susan_weight_hypothesis = 80
ann_weight_premise = 0
ann_weight_hypothesis = 0
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis refers to the weight of Susan and Anna, mentioned in the premise
if (susan_weight_hypothesis + ann_weight_hypothesis)!= total_weight_premise:
    # check if the sum of the weights of Susan and Anna in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
elif (susan_weight_premise + ann_weight_premise)!= total_weight_hypothesis:
    # check if the total weight of Susan and Anna in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
