susan_weight_premise = 40
susan_weight_hypothesis = 10
anna_weight_premise = 10
anna_weight_hypothesis = 10
total_weight_premise = 110
total_weight_hypothesis = 110

# the hypothesis talks about the weights of Susan and Anna, which are also mentioned in the premise
if susan_weight_hypothesis > susan_weight_premise:
    # check if the hypothesis value of Susan's weight contradicts the estimate of less than'susan_weight_premise'
    label = "contradiction"
elif anna_weight_hypothesis!= anna_weight_premise:
    # check if the hypothesis value of Anna's weight contradicts the estimate of 'anna_weight_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
