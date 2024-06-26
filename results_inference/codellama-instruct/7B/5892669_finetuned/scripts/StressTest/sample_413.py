ratio_premise = 1/2
ratio_hypothesis = 1/2

# the hypothesis refers to the ratio of ages of Lewis and Brown mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis is less than the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
