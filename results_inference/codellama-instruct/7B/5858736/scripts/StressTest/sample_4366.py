# Define variables with representative names for the numerical entities in both inputs
x_premise = 0
x_hypothesis = 0
hours_worked_premise = 0
hours_worked_hypothesis = 0

# Extract all quantities as valid numbers (integers or floats)
x_premise = float(input("Enter the value of x in the premise: "))
hours_worked_premise = float(input("Enter the number of hours worked in the premise: "))
x_hypothesis = float(input("Enter the value of x in the hypothesis: "))
hours_worked_hypothesis = float(input("Enter the number of hours worked in the hypothesis: "))

# Use brief comments to explain what comparison you do between the defined variables
if hours_worked_premise <= 60:
    # Check if the number of hours worked in the premise is less than or equal to 60
    if hours_worked_hypothesis <= 60:
        # Check if the number of hours worked in the hypothesis is less than or equal to 60
        if x_premise == x_hypothesis:
            # Check if the value of x in the premise is equal to the value of x in the hypothesis
            label = "entailment"
        else:
            # Check if the value of x in the premise is not equal to the value of x in the hypothesis
            label = "contradiction"
    else:
        # Check if the number of hours worked in the hypothesis is greater than 60
        label = "contradiction"
else:
    # Check if the number of hours worked in the premise is greater than 60
    if hours_worked_hypothesis <= 60:
        # Check if the number of hours worked in the hypothesis is less than or equal to 60
        label = "neutral"
    else:
        # Check if the number of hours worked in the hypothesis is greater than 60
        label = "contradiction"

print(label)
