# Define variables with representative names for the numerical entities in both inputs
x_premise = 40
x_hypothesis = 70
hourly_wage_premise = 1.0 * x_premise
hourly_wage_hypothesis = 1.5 * x_hypothesis

# Extract all quantities as valid numbers (integers or floats)
hourly_wage_premise = float(hourly_wage_premise)
hourly_wage_hypothesis = float(hourly_wage_hypothesis)

# Perform calculations if necessary
hourly_wage_diff = hourly_wage_hypothesis - hourly_wage_premise

# Compare the variables and infer the label
if hourly_wage_diff > 0:
    label = "entailment"
elif hourly_wage_diff == 0:
    label = "neutral"
else:
    label = "contradiction"

print(label)
