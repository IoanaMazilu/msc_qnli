# Define variables with representative names for the numerical entities in both inputs
total_hours_last_week_james = 41
total_hours_last_week_harry = 11

# Extract all quantities as valid numbers (integers or floats)
total_hours_last_week_james = int(total_hours_last_week_james)
total_hours_last_week_harry = int(total_hours_last_week_harry)

# Use brief comments to explain what comparison you do between the defined variables
if total_hours_last_week_james > total_hours_last_week_harry:
    # Check if the hypothesis value contradicts the estimate of more than 'total_hours_last_week_harry'
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of hours worked last week
    # Any number of hours greater than 'total_hours_last_week_harry' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
