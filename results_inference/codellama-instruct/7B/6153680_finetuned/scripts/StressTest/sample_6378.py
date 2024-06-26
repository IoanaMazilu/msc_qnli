x_premise = 10
x_hypothesis = 10

# the hypothesis refers to the same situation as the premise, but with a different number of hours
if x_hypothesis <= x_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
