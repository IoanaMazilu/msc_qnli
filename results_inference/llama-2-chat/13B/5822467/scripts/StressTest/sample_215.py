# Define variables with representative names for the numerical entities in both inputs
average_speed_premise = 36
tom_speed_hypothesis = 36

# Extract all quantities as valid numbers (integers or floats)
if average_speed_premise > tom_speed_hypothesis:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif tom_speed_hypothesis < average_speed_premise:
    # Check if the hypothesis value is consistent with the premise value
    label = "entailment"
else:
    # If the hypothesis value is equal to the premise value, there is no contradiction or entailment
    label = "neutral"

print(label)
