# Define variables with representative names for the numerical entities in both inputs
hours_premise = x
hours_hypothesis = 52
pay_per_hour_premise = 1.5 * hours_premise
pay_per_hour_hypothesis = 1.5 * hours_hypothesis

# Extract all quantities as valid numbers
hours_premise = int(hours_premise)
hours_hypothesis = int(hours_hypothesis)
pay_per_hour_premise = float(pay_per_hour_premise)
pay_per_hour_hypothesis = float(pay_per_hour_hypothesis)

# Compare the variables
if hours_premise <= hours_hypothesis:
    # Check if the estimate of 'hours_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
elif pay_per_hour_hypothesis!= pay_per_hour_premise:
    # Check if the pay per hour in the hypothesis contradicts the pay per hour reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
