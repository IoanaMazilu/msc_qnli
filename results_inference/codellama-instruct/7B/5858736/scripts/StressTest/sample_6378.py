# Define variables with representative names for the numerical entities in both inputs
x_premise = 0
x_hypothesis = 0
hours_premise = 0
hours_hypothesis = 0

# Extract all quantities as valid numbers (integers or floats)
x_premise = float(input("Enter the hourly wage for the first 30 hours: "))
hours_premise = int(input("Enter the number of hours worked in the first 30 hours: "))
x_hypothesis = float(input("Enter the hourly wage for the first more than 10 hours: "))
hours_hypothesis = int(input("Enter the number of hours worked in the first more than 10 hours: "))

# Use brief comments to explain what comparison you do between the defined variables
if hours_premise <= hours_hypothesis:
    # Check if the estimate of 'hours_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
elif x_hypothesis!= x_premise:
    # Check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
