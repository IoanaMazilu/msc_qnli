susan_weight_premise = 10
susan_weight_hypothesis = 40
annas_weight_premise = 0
annas_weight_hypothesis = 0
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis refers to the weight of Susan and Anna, mentioned in the premise
if (susan_weight_premise + annas_weight_premise) <= (susan_weight_hypothesis + annas_weight_hypothesis):
    # check if the estimate of'susan_weight_hypothesis' and 'annas_weight_hypothesis' contradicts the weight of Susan and Anna in the premise
    label = "contradiction"
elif (susan_weight_premise + annas_weight_premise)!= total_weight_premise:
    # check if the total weight of Susan and Anna in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
