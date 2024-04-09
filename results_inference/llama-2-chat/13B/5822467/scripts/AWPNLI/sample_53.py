# Define variables for numerical entities in the premise and hypothesis
lambs_premise = 6048.0
white_lambs_premise = 193.0
black_lambs_hypothesis = 5854.0

# Extract all quantities as valid numbers
lambs_premise = float(lambs_premise)
white_lambs_premise = float(white_lambs_premise)
black_lambs_hypothesis = float(black_lambs_hypothesis)

# Perform calculations if necessary
total_lambs_premise = lambs_premise + white_lambs_premise

# Compare the variables
if black_lambs_hypothesis > total_lambs_premise:
    # The hypothesis contradicts the premise
    label = "contradiction"
elif black_lambs_hypothesis < total_lambs_premise:
    # The hypothesis is entailed by the premise
    label = "entailment"
else:
    # No comparison is needed, the premise and hypothesis are neutral
    label = "neutral"

print(label)
