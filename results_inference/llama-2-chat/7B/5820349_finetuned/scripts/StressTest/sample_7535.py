leo_weight_gain_premise = 10
leo_weight_gain_hypothesis = 80

# the hypothesis refers to the weight gain of Leo, which is also mentioned in the premise
if leo_weight_gain_hypothesis!= leo_weight_gain_premise:
    # check if the weight gain of Leo in the hypothesis contradicts the weight gain mentioned in the premise
    label = "contradiction"
else:
    # if the weight gain of Leo in the hypothesis does not contradict the weight gain mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)
