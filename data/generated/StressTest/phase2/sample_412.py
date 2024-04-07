# Premise: The present ages of Lewis and Brown are in the ratio less than 8:2.
# Hypothesis: The present ages of Lewis and Brown are in the ratio 1:2.
# Golden Label: neutral

lewis_brown_ratio_premise = 8 / 2
lewis_brown_ratio_hypothesis = 1 / 2

# the hypothesis refers to the age ratio of Lewis and Brown mentioned in the premise
if lewis_brown_ratio_hypothesis >= lewis_brown_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif lewis_brown_ratio_hypothesis == lewis_brown_ratio_premise:
    # check if the age ratio in the hypothesis is the same as the ratio in the premise
    label = "entailment"
else:
    # if the age ratio in the hypothesis does not contradict the one in the premise, we cannot infer entailment or contradiction,
    # so the relation is neutral
    label = "neutral"

print(label)

