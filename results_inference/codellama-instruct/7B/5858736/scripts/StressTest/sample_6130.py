# Define variables with representative names for the numerical entities in both inputs
x_premise = 0
x_hypothesis = 0
hours_premise = 0
hours_hypothesis = 0

# Extract all quantities as valid numbers (integers or floats)
x_premise = float(input("Enter the value of x in the premise: "))
hours_premise = float(input("Enter the number of hours worked in the premise: "))
x_hypothesis = float(input("Enter the value of x in the hypothesis: "))
hours_hypothesis = float(input("Enter the number of hours worked in the hypothesis: "))

# Use brief comments to explain what comparison you do between the defined variables
if hours_premise <= 11:
    # Check if the number of hours worked in the premise is less than or equal to 11
    # If so, the hypothesis value contradicts the premise
    label = "contradiction"
elif hours_hypothesis <= 11:
    # Check if the number of hours worked in the hypothesis is less than or equal to 11
    # If so, the hypothesis value contradicts the premise
    label = "contradiction"
elif hours_premise > 11 and hours_hypothesis > 11:
    # Check if the number of hours worked in the premise is greater than 11 and the number of hours worked in the hypothesis is also greater than 11
    # If so, the hypothesis value is consistent with the premise
    label = "neutral"
else:
    # If the number of hours worked in the premise is greater than 11 and the number of hours worked in the hypothesis is less than or equal to 11,
    # the hypothesis value contradicts the premise
    label = "contradiction"

print(label)
