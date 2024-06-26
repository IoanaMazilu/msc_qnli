ratio_premise = 3/2
ratio_hypothesis = 2/2

# the hypothesis refers to the ratio of prices of a car and AC mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
