# Define variables with representative names for the numerical entities in both inputs
average_speed_premise = 4/2
average_speed_hypothesis = 1/2

# Extract all quantities as valid numbers (integers or floats)
average_speed_premise = float(average_speed_premise)
average_speed_hypothesis = float(average_speed_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
# Use the correct comparison operators

# Check if the hypothesis value contradicts the estimate of the premise
if average_speed_hypothesis > average_speed_premise:
    # The hypothesis value is greater than the estimate of the premise, so we have a contradiction
    label = "contradiction"

# Check if the estimate of the premise is greater than the hypothesis value
elif average_speed_premise > average_speed_hypothesis:
    # The estimate of the premise is greater than the hypothesis value, so we have an entailment
    label = "entailment"

# If the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
else:
    label = "neutral"

print(label)
