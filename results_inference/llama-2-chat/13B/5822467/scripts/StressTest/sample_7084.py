# Define variables with representative names for the numerical entities in both inputs
annie_working_time_premise = 20
annie_working_time_hypothesis = 10

# Extract all quantities as valid numbers (integers or floats)
# and perform calculations if necessary

# Compare the variables to infer one of the following:
# entailment, contradiction, or neutral

# Check if the hypothesis value contradicts the estimate in the premise
if annie_working_time_hypothesis <= annie_working_time_premise:
    # The hypothesis value contradicts the estimate in the premise
    label = "contradiction"

# Check if the hypothesis value is less than the estimate in the premise
if annie_working_time_hypothesis < annie_working_time_premise:
    # The hypothesis value is less than the estimate in the premise
    label = "entailment"

else:
    # The hypothesis value is greater than or equal to the estimate in the premise
    # The premise only gives an estimate, so any value greater than the estimate is consistent with the premise
    label = "neutral"

print(label)
