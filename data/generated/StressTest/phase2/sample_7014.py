# Premise: The present ages of Lewis and Brown are in the ratio 1:2.
# Hypothesis: The present ages of Lewis and Brown are in the ratio less than 6:2.
# Golden Label: entailment

ratio_premise = 1/2
ratio_hypothesis = 6/2

# The hypothesis refers to the age ratio of Lewis and Brown mentioned in the premise
if ratio_hypothesis > ratio_premise:
    # Check if the ratio in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
elif ratio_hypothesis < ratio_premise:
    # Check if the ratio in the hypothesis is less than the ratio reported in the premise
    label = "entailment"
else:
    # If the ratio in the hypothesis is equal to the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)

