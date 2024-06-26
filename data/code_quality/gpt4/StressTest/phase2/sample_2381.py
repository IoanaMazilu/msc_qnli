ratio_premise = [2, 3]
ratio_hypothesis = [4, 3]

# The hypothesis refers to the same scenario as the premise, but gives different ratio values.
if ratio_premise != ratio_hypothesis:
    # If the ratio in the hypothesis contradicts the ratio in the premise, we have a contradiction.
    label = "contradiction"
else:
    # If the ratios are the same, the hypothesis is entailed by the premise.
    label = "entailment"

print(label)
