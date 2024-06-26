# Define variables with representative names for the numerical entities in both inputs
t_premise = 5/9 * (k_premise - 32)
t_hypothesis = less than 5/9 * (k_hypothesis - 32)
k_premise = 105

# Extract all quantities as valid numbers (integers or floats)
t_premise = float(t_premise)
t_hypothesis = float(t_hypothesis)
k_premise = int(k_premise)

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments

# Compare the two expressions for T
if t_hypothesis < t_premise:
    # The hypothesis contradicts the premise
    label = "contradiction"
elif t_hypothesis > t_premise:
    # The hypothesis entails the premise
    label = "entailment"
else:
    # The hypothesis and premise are neutral
    label = "neutral"

# Compare the two expressions for K
if k_premise == k_hypothesis:
    # The hypothesis and premise are neutral
    label = "neutral"
elif k_premise < k_hypothesis:
    # The hypothesis entails the premise
    label = "entailment"
else:
    # The hypothesis contradicts the premise
    label = "contradiction"

# Print the label
print(label)
