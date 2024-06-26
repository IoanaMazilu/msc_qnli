# Define variables for the numerical entities in the premise and hypothesis
premise_hourly_wage = 12
premise_additional_hourly_wage = 1.5
hypothesis_hourly_wage = 52
hypothesis_additional_hourly_wage = 1.5

# Extract all quantities as valid numbers
premise_total_wage = premise_hourly_wage * 12 + premise_additional_hourly_wage * 12
hypothesis_total_wage = hypothesis_hourly_wage * 52 + hypothesis_additional_hourly_wage * 12

# Check if the hypothesis values contradict the premise ones
if hypothesis_total_wage <= premise_total_wage:
    label = "contradiction"
else:
    # The hypothesis values do not contradict the premise ones, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
