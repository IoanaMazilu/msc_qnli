# Premise: The present ages of Lewis and Brown are in the ratio 1:2.
# Hypothesis: The present ages of Lewis and Brown are in the ratio less than 1:2.
# Golden Label: contradiction

ratio_premise = 1 / 2
ratio_hypothesis = ratio_premise - 0.1  # assuming the hypothesis ratio is less than 1:2

# the hypothesis refers to the same ratio of ages as in the premise
if ratio_hypothesis > ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
elif ratio_hypothesis == ratio_premise:
    # check if the ratio in the hypothesis is the same as the ratio in the premise
    label = "entailment"
else:
    # if the ratio in the hypothesis is less than the ratio in the premise, it does not contradict the premise but cannot be fully entailed from it either
    label = "neutral"

print(label)

