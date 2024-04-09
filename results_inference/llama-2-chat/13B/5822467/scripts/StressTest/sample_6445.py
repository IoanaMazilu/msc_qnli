# Define variables with representative names for the numerical entities in both inputs
age_premise = 84
age_hypothesis = 14

# Extract all quantities as valid numbers (integers or floats)
age_premise_int = int(age_premise)
age_hypothesis_int = int(age_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
# Note: do not use their values in the comments

# Check if the hypothesis value contradicts the premise estimate
if age_hypothesis_int > age_premise_int:
    # Check if the hypothesis value contradicts the premise estimate
    label = "contradiction"
elif age_hypothesis_int == age_premise_int:
    # The hypothesis value is consistent with the premise estimate
    label = "neutral"
else:
    # The hypothesis value is less than the premise estimate
    label = "entailment"

print(label)
