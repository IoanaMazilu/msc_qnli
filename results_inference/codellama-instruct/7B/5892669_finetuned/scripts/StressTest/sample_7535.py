weight_gain_leo_premise = 10
weight_gain_leo_hypothesis = 80

# the hypothesis refers to the weight gain of Leo mentioned in the premise
if weight_gain_leo_hypothesis!= weight_gain_leo_premise:
    # check if the weight gain of Leo in the hypothesis contradicts the weight gain reported in the premise
    label = "contradiction"
else:
    # if the weight gain of Leo in the hypothesis does not contradict the weight gain reported in the premise, we can infer entailment
    label = "entailment"

print(label)
