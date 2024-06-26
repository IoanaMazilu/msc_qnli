# Define variables with representative names for the numerical entities in both inputs
samsung_premise = 75
iphone_premise = 70
samsung_hypothesis = 85
iphone_hypothesis = 25

# Extract all quantities as valid numbers (integers or floats)
samsung_premise = float(samsung_premise)
iphone_premise = float(iphone_premise)
samsung_hypothesis = float(samsung_hypothesis)
iphone_hypothesis = float(iphone_hypothesis)

# Perform calculations if necessary
samsung_diff = samsung_hypothesis - samsung_premise
iphone_diff = iphone_hypothesis - iphone_premise

# Compare the variables to infer the label
if samsung_diff > 0 and iphone_diff > 0:
    # The hypothesis is consistent with the premise, so the label is neutral
    label = "neutral"
elif samsung_diff > 0 and iphone_diff == 0:
    # The hypothesis contradicts the premise, so the label is contradiction
    label = "contradiction"
elif samsung_diff == 0 and iphone_diff > 0:
    # The hypothesis is consistent with the premise, so the label is entailment
    label = "entailment"
else:
    # The hypothesis and premise have the same value, so the label is neutral
    label = "neutral"

# Print the label
print(label)
