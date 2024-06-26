leo_gain_weight_premise = 10
leo_gain_weight_hypothesis = 50

# the hypothesis refers to the weight gain of Leo mentioned in the premise
if leo_gain_weight_hypothesis < leo_gain_weight_premise:
    # check if the estimate of 'leo_gain_weight_hypothesis' contradicts the weight gain in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
