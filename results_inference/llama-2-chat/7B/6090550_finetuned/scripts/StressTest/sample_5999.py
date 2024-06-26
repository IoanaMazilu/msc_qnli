# The hypothesis refers to the same condition as the premise, but with different ratios.

# The premise states that a film must appear in at least 1/4 of the top-10-movies lists.
# The hypothesis states that a film must appear in at least 6/4 of the top-10-movies lists.

# Convert both ratios to decimals.
ratio_premise = 1/4
ratio_hypothesis = 6/4

# Check if the ratio in the hypothesis contradicts the ratio in the premise.
if ratio_hypothesis <= ratio_premise:
    label = "contradiction"
else:
    # If the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment.
    label = "entailment"

print(label)
