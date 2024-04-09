leo_weight_premise = 10
leo_weight_hypothesis = 50
kendra_weight_premise = 50

# the hypothesis refers to the weight gain of Leo and the premise mentions the weight of Kendra
if leo_weight_hypothesis <= kendra_weight_premise:
    # check if the estimate of 'leo_weight_hypothesis' contradicts the weight of Kendra in the premise
    label = "contradiction"
elif leo_weight_hypothesis > 50:
    # check if the weight gain of Leo in the hypothesis contradicts the premise statement
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
