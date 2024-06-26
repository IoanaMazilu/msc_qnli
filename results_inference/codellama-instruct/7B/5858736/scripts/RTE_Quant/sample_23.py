# Define variables with representative names for the numerical entities in both inputs
peak_height_premise = 8586
peak_height_hypothesis = 8586

# Extract all quantities as valid numbers (integers or floats)
peak_height_premise = float(peak_height_premise)
peak_height_hypothesis = float(peak_height_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if peak_height_hypothesis!= peak_height_premise:
    # Check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
