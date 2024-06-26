susan_weight_premise = 10
anna_weight_premise = 10
total_weight_premise = 110

susan_weight_hypothesis = 80
anna_weight_hypothesis = 10
total_weight_hypothesis = 110

# the hypothesis refers to the weights of Susan and Anna, and the total weight mentioned in the premise
if susan_weight_hypothesis!= susan_weight_premise:
    # check if the hypothesis value for Susan's weight contradicts the premise value
    label = "contradiction"
elif anna_weight_hypothesis!= anna_weight_premise:
    # check if the hypothesis value for Anna's weight contradicts the premise value
    label = "contradiction"
elif total_weight_hypothesis!= total_weight_premise:
    # check if the hypothesis value for the total weight contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
