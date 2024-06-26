# Define variables with representative names for the numerical entities in both inputs
x_premise = 0
x_hypothesis = 0
hours_premise = 0
hours_hypothesis = 0

# Extract all quantities as valid numbers (integers or floats)
x_premise = float(input("Enter the value of x in the premise: "))
hours_premise = int(input("Enter the number of hours worked in the premise: "))
x_hypothesis = float(input("Enter the value of x in the hypothesis: "))
hours_hypothesis = int(input("Enter the number of hours worked in the hypothesis: "))

# Use brief comments to explain what comparison you do between the defined variables
if hours_premise <= 24:
    # Check if the number of hours worked in the premise is less than or equal to 24
    if x_premise * hours_premise <= x_hypothesis * hours_hypothesis:
        # Check if the estimate of 'x_hypothesis' contradicts the number of hours worked in the premise
        label = "contradiction"
    else:
        # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
        label = "entailment"
else:
    # If the number of hours worked in the premise is greater than 24, we can infer neutrality
    label = "neutral"

print(label)
