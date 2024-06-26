susan_weight_premise = 10
anna_weight_premise = 10
total_weight_premise = 110

# the hypothesis talks about the weight difference between Susan and Anna, which is also mentioned in the premise
if susan_weight_hypothesis <= susan_weight_premise:
    # check if the hypothesis value contradicts the estimate of'susan_weight_premise'
    label = "contradiction"
elif anna_weight_hypothesis!= anna_weight_premise:
    # check if the estimate of 'anna_weight_hypothesis' contradicts the number of weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
