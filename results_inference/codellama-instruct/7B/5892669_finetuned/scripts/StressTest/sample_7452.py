T_premise = 105
T_hypothesis = 105
K_premise = 0
K_hypothesis = 0

# the hypothesis refers to the same situation as the premise, but with a different equation for T
if T_premise!= T_hypothesis:
    # check if the value of T in the hypothesis contradicts the value of T in the premise
    label = "contradiction"
elif T_premise == T_hypothesis:
    # check if the value of T in the hypothesis is equal to the value of T in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
