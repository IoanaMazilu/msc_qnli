T_premise = 20
T_hypothesis = 20
K_premise = 0
K_hypothesis = 0

# the hypothesis refers to the same situation as the premise, but with a different equation for T
if T_premise!= T_hypothesis:
    # check if the value of T in the hypothesis contradicts the value of T in the premise
    label = "contradiction"
elif K_premise!= K_hypothesis:
    # check if the value of K in the hypothesis contradicts the value of K in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
