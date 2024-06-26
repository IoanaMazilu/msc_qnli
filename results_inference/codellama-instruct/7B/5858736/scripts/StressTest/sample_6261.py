# Define variables with representative names for the numerical entities in both inputs
annie_hours_premise = 10
annie_hours_hypothesis = 40

# Extract all quantities as valid numbers (integers or floats)
annie_hours_premise = float(annie_hours_premise)
annie_hours_hypothesis = float(annie_hours_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if annie_hours_hypothesis <= annie_hours_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'annie_hours_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of hours
    # Any number of hours greater than 'annie_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
