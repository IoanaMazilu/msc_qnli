ratio_premise = 1
ratio_hypothesis = 6

# check if the ratio in the hypothesis is consistent with the ratio in the premise
if ratio_hypothesis <= ratio_premise:
    # the ratio in the hypothesis is consistent with the ratio in the premise, so entailment
    label = "entailment"
elif ratio_hypothesis > ratio_premise:
    # the ratio in the hypothesis contradicts the ratio in the premise, so contradiction
    label = "contradiction"
else:
    # the ratio in the hypothesis is neither consistent nor inconsistent with the ratio in the premise, so neutral
    label = "neutral"

print(label)
