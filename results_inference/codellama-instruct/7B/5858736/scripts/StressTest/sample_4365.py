# Define variables with representative names for the numerical entities in both inputs
x_premise = 10
x_hypothesis = 12
hours_worked_premise = 40
hours_worked_hypothesis = 60

# Extract all quantities as valid numbers (integers or floats)
x_premise = float(x_premise)
x_hypothesis = float(x_hypothesis)
hours_worked_premise = float(hours_worked_premise)
hours_worked_hypothesis = float(hours_worked_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if x_premise == x_hypothesis:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif hours_worked_hypothesis < hours_worked_premise:
    # Check if the number of hours worked in the hypothesis contradicts the number of hours worked reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
