ratio_premise = 10 / 5
ratio_hypothesis = 30 / 5

# the hypothesis refers to the ratio of distances mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif ratio_hypothesis > ratio_premise:
    # if the ratio in the hypothesis is more than the ratio in the premise, it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the ratio in the hypothesis matches the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
