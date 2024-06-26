# Define variables with representative names for the numerical entities in both inputs
total_hours_last_week_premise = 61
total_hours_last_week_hypothesis = 41

# Extract all quantities as valid numbers (integers or floats)
total_hours_last_week_premise = int(total_hours_last_week_premise)
total_hours_last_week_hypothesis = int(total_hours_last_week_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if total_hours_last_week_hypothesis <= total_hours_last_week_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'total_hours_last_week_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of hours worked last week
    # Any number of hours greater than 'total_hours_last_week_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
