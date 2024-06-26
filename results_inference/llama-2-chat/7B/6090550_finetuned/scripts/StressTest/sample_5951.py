T_premise = 5/9 * (K-32)
T_hypothesis = less_than(5/9 * (K-32), 20)

# the hypothesis refers to the same situation as the premise
if T_premise!= T_hypothesis:
    # check if the value of T in the hypothesis contradicts the value of T in the premise
    label = "contradiction"
else:
    # if the values of T in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
