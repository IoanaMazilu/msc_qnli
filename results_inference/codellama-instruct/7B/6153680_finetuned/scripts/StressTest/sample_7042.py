susan_weight_premise = 40
susan_weight_hypothesis = 10
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis talks about the weight of Susan and Anna, which is also mentioned in the premise
if susan_weight_hypothesis + susan_weight_premise > total_weight_premise:
    # check if the total weight of Susan and Anna in the hypothesis contradicts the total weight in the premise
    label = "contradiction"
elif susan_weight_hypothesis + susan_weight_premise < total_weight_premise:
    # check if the total weight of Susan and Anna in the hypothesis is less than the total weight in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
