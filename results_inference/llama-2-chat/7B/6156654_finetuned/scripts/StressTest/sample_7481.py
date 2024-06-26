# Define variables for the premise and hypothesis
hours_first_week = 24
hours_second_week = 54
multiplier_first_week = 1.5
multiplier_second_week = 1.5

# Calculate the total pay for the first week
total_pay_first_week = hours_first_week * multiplier_first_week

# Calculate the total pay for the second week
total_pay_second_week = hours_second_week * multiplier_second_week

# Check if the total pay for the second week is greater than the total pay for the first week
if total_pay_second_week > total_pay_first_week:
    # The hypothesis contradicts the premise
    label = "contradiction"
else:
    # The hypothesis is consistent with the premise
    label = "entailment"

print(label)
