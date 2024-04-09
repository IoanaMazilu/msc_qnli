# Define variables with representative names for the numerical entities in both inputs
deficit_premise = 5120000000
deficit_hypothesis = 1000000000

# Extract all quantities as valid numbers (integers or floats)
deficit_premise = int(deficit_premise)
deficit_hypothesis = int(deficit_hypothesis)

# Compare the variables
if deficit_hypothesis!= deficit_premise:
    # Check if the hypothesis contradicts the premise
    label = "contradiction"
elif deficit_hypothesis < deficit_premise:
    # Check if the hypothesis is less than the premise
    label = "entailment"
else:
    # The hypothesis is greater than or equal to the premise, so the label is neutral
    label = "neutral"

print(label)
