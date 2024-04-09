# Define variables with representative names for the numerical entities in both inputs
maxwell_walking_speed = 4
brad_running_speed = 6
distance_premise = 40

# Extract all quantities as valid numbers (integers or floats)
distance_hypothesis = float(input("Enter the distance between their homes: "))

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments

# Compare the distance in the hypothesis to the distance in the premise
if distance_hypothesis > distance_premise:
    # The hypothesis refers to a distance greater than the premise, so we can infer entailment
    label = "entailment"
elif distance_hypothesis <= distance_premise:
    # The hypothesis refers to a distance less than or equal to the premise, so we can infer contradiction
    label = "contradiction"
else:
    # The hypothesis refers to a distance equal to the premise, so we can infer neutrality
    label = "neutral"

# Print the label
print(label)
