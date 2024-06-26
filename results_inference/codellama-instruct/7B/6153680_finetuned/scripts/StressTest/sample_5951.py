T_premise = 5/9 * (K-32)
T_hypothesis = 5/9 * (K-32)
T_value = 20

# the hypothesis refers to the same formula for T as the premise
if T_hypothesis < T_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
