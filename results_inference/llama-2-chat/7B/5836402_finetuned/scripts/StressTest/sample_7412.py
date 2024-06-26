butter_weight_premise = 27
butter_weight_hypothesis = 77

# the hypothesis refers to the weight of butter mixed, which is also mentioned in the premise
if butter_weight_hypothesis!= butter_weight_premise:
    # check if the weight of butter in the hypothesis contradicts the weight of butter reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
