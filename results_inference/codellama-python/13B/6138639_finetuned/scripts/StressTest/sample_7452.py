T_premise = 5/9 * (K-32)
T_hypothesis = 4/9 * (K-32)
T_value = 105

# the hypothesis refers to the value of T mentioned in the premise
if T_value <= T_hypothesis:
    # check if the value of 'T_hypothesis' contradicts the value of T in the premise
    label = "contradiction"
elif T_value == T_premise:
    # check if the value of T in the hypothesis is equal to the value of T in the premise
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
