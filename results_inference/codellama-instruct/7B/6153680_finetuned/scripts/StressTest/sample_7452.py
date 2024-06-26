T_premise = 5/9 * (K-32)
T_hypothesis = 4/9 * (K-32)
T_value = 105

# the hypothesis refers to the same temperature T as in the premise
if T_hypothesis >= T_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
