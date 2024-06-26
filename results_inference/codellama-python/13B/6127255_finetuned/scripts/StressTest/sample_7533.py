leo_gain_premise = 10
leo_gain_hypothesis = 50
weight_percentage_difference = 50

# the hypothesis refers to the weight gain of Leo mentioned in the premise
if leo_gain_hypothesis <= leo_gain_premise:
    # check if the weight gain estimate in the hypothesis contradicts the weight gain in the premise
    label = "contradiction"
else:
    # if the weight gain estimate in the hypothesis does not contradict the weight gain in the premise, we can infer entailment
    label = "entailment"

print(label)
