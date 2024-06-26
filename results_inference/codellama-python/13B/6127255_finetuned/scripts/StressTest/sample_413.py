lewis_brown_ratio_premise = 1/2
lewis_brown_ratio_hypothesis = 1/2

# the hypothesis refers to the age ratio of Lewis and Brown mentioned in the premise
if lewis_brown_ratio_hypothesis >= lewis_brown_ratio_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
