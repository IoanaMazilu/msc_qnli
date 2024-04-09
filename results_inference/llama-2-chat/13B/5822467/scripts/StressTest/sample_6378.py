# Define variables for numerical entities in the premise and hypothesis
hours_premise = 30
hourly_wage_premise = x
additional_hourly_wage_premise = 1.5
total_hours_premise = hours_premise + 10

hours_hypothesis = 10
hourly_wage_hypothesis = x
additional_hourly_wage_hypothesis = 1.5
total_hours_hypothesis = hours_hypothesis + 10

# Perform calculations
hourly_wage_total_premise = hourly_wage_premise * total_hours_premise
additional_hourly_wage_total_premise = additional_hourly_wage_premise * (total_hours_premise - hours_premise)

hourly_wage_total_hypothesis = hourly_wage_hypothesis * total_hours_hypothesis
additional_hourly_wage_total_hypothesis = additional_hourly_wage_hypothesis * (total_hours_hypothesis - hours_hypothesis)

# Compare the calculated values
if hourly_wage_total_premise <= hourly_wage_total_hypothesis:
    label = "entailment"
elif hourly_wage_total_hypothesis!= hourly_wage_total_premise:
    label = "contradiction"
else:
    label = "neutral"

if additional_hourly_wage_total_premise!= additional_hourly_wage_total_hypothesis:
    label = "contradiction"

print(label)
