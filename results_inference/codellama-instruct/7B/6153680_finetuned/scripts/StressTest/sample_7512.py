shirts_premise = 1
jeans_premise = 1
sneakers_premise = 1

shirts_hypothesis = 4
jeans_hypothesis = 1
sneakers_hypothesis = 1

# the hypothesis refers to the same outfit as the premise
if shirts_hypothesis <= shirts_premise and jeans_hypothesis == jeans_premise and sneakers_hypothesis == sneakers_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
