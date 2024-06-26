# Define variables with representative names for the numerical entities in both inputs
hours_travelled_premise = 10
hours_travelled_hypothesis = 20

# Extract all quantities as valid numbers (integers or floats)
hours_travelled_premise = int(hours_travelled_premise)
hours_travelled_hypothesis = int(hours_travelled_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if hours_travelled_hypothesis <= hours_travelled_premise:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
