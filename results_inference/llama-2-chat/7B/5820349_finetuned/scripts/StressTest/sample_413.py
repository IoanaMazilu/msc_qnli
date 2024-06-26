lewis_brown_ratio_premise = 1/2
lewis_brown_ratio_hypothesis = 1/2

# the hypothesis refers to the ratio of ages of Lewis and Brown mentioned in the premise
if lewis_brown_ratio_hypothesis >= lewis_brown_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)
