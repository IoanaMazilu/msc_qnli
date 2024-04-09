susan_weight_premise = 40 + anna_weight_premise
anna_weight_premise = 110 - susan_weight_premise

susan_weight_hypothesis = 10 + anna_weight_hypothesis

# the hypothesis refers to the difference in weight between Susan and Anna
if susan_weight_hypothesis <= anna_weight_premise:
    # check if the estimate of 'anna_weight_premise' contradicts the difference in weight between Susan and Anna in the hypothesis
    label = "contradiction"
elif susan_weight_hypothesis!= anna_weight_hypothesis:
    # check if the difference in weight between Susan and Anna in the hypothesis contradicts the difference in weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
