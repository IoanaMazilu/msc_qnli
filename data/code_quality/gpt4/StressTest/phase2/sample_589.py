ratio_premise = 4/9
ratio_hypothesis = 5/9

# the hypothesis refers to a ratio between the ages of Neelam and Shaan, which is also mentioned in the premise
if ratio_hypothesis != ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis doesn't contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
