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
if hours_premise <= hours_hypothesis:
    # Check if the estimate of 'hours_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
elif x_hypothesis!= x_premise:
    # Check if the value of x in the hypothesis contradicts the value of x in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
