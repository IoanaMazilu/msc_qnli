ratio_premise = [3, 3]
ratio_hypothesis = [7, 3]

# the hypothesis refers to the ratio of distances between points A, B and C, mentioned in the premise
if ratio_hypothesis != ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
