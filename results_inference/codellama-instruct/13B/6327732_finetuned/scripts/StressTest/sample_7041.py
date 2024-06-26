susan_weight_premise = 10
anna_weight_premise = 110 - susan_weight_premise

susan_weight_hypothesis = 40
anna_weight_hypothesis = susan_weight_hypothesis + susan_weight_premise

# the hypothesis refers to the difference in weight between Susan and Anna
if susan_weight_hypothesis <= susan_weight_premise:
    # check if the hypothesis value contradicts the estimate of more than'susan_weight_premise'
    label = "contradiction"
elif anna_weight_hypothesis!= anna_weight_premise:
    # check if the hypothesis value contradicts the number of pies sold in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
