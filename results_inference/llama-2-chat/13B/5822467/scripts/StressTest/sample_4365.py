# Define variables with representative names for the numerical entities in both inputs
x_premise = 40
x_hypothesis = 60

# Extract all quantities as valid numbers (integers or floats)
x_premise = int(x_premise)
x_hypothesis = int(x_hypothesis)

# Perform calculations if necessary
hours_worked_premise = x_premise * 2
hours_worked_hypothesis = x_hypothesis * 2

# Compare the variables
if hours_worked_premise <= hours_worked_hypothesis:
    # Check if the estimate of 'hours_worked_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
elif hours_worked_hypothesis!= hours_worked_premise:
    # Check if the number of hours worked in the hypothesis contradicts the number of hours worked reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
