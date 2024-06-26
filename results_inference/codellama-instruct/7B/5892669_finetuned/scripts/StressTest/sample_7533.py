weight_gain_leo_premise = 10
weight_gain_leo_hypothesis = 50

# the hypothesis refers to the weight gain of Leo mentioned in the premise
if weight_gain_leo_hypothesis <= weight_gain_leo_premise:
    # check if the estimate of 'weight_gain_leo_hypothesis' contradicts the weight gain of Leo in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
