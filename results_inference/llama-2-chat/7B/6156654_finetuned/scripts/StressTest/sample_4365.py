# Define variables for the premise
hours_first_40 = 40
additional_hours = hours_first_40 + 60
pay_rate_first_40 = x
pay_rate_additional = 2 * x

# Define hypothesis variables
hours_less_than_60 = additional_hours - 60
pay_rate_hours_less_than_60 = x
pay_rate_additional_hours = 2 * x

# Check if the hypothesis contradicts the premise
if additional_hours <= hours_first_40:
    label = "contradiction"
elif pay_rate_hours_less_than_60!= pay_rate_additional_hours:
    label = "contradiction"
else:
    label = "neutral"

print(label)
