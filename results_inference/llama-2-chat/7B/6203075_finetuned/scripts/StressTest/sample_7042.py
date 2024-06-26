susan_weight_premise = 40
susan_weight_hypothesis = 10
anna_weight_premise = 10
anna_weight_hypothesis = 10
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis talks about the weight difference between Susan and Anna, and the total weight
if susan_weight_hypothesis < susan_weight_premise:
    # check if the weight difference in the hypothesis contradicts the weight difference in the premise
    label = "contradiction"
elif anna_weight_hypothesis!= anna_weight_premise:
    # check if the weight of Anna in the hypothesis contradicts the weight of Anna in the premise
    label = "contradiction"
elif total_weight_hypothesis!= total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
