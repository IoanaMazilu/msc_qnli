# Define variables with representative names for the numerical entities in both inputs
x_premise = 0
x_hypothesis = 0
hours_premise = 0
hours_hypothesis = 0

# Extract all quantities as valid numbers (integers or floats)
x_premise = float(input("Enter the hourly wage for the first 35 hours: "))
hours_premise = int(input("Enter the number of hours worked in the first week: "))
x_hypothesis = float(input("Enter the hourly wage for the first more than 35 hours: "))
hours_hypothesis = int(input("Enter the number of hours worked in the second week: "))

# Use brief comments to explain what comparison you do between the defined variables
if hours_premise <= 35:
    # Check if the hypothesis value contradicts the number of hours worked in the premise
    if x_hypothesis!= x_premise:
        label = "contradiction"
    else:
        # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
        label = "entailment"
else:
    # If the hypothesis value is greater than 35, we can infer neutrality
    label = "neutral"

print(label)
