x_premise = 15
x_hypothesis = 15

# the hypothesis refers to the same situation as the premise
if x_hypothesis >= x_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
