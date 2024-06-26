T_premise = 105
T_hypothesis = 105

# the hypothesis refers to the same equation as the premise, but with a different condition
if T_premise == T_hypothesis:
    # if the values of T in the premise and hypothesis are the same, we can infer entailment
    label = "entailment"
else:
    # if the values of T are different, we cannot infer entailment since the hypothesis condition is not met
    label = "contradiction"

print(label)
