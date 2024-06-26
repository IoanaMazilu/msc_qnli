# Define variables with representative names for the numerical entities in both inputs
matthew_walk_premise = "35 km"
johnny_walk_hypothesis = "45 km"

# Extract all quantities as valid numbers (integers or floats)
matthew_walk_premise = int(matthew_walk_premise)
johnny_walk_hypothesis = int(johnny_walk_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
# (do not use their values in the comments)

# Compare the two distances
if johnny_walk_hypothesis > matthew_walk_premise:
    # The hypothesis states a distance greater than the premise, so we can infer entailment
    label = "entailment"
elif johnny_walk_hypothesis <= matthew_walk_premise:
    # The hypothesis states a distance less than or equal to the premise, so we can infer contradiction
    label = "contradiction"
else:
    # The hypothesis states a distance equal to the premise, so we can infer neutrality
    label = "neutral"

# Print the label
print(label)
