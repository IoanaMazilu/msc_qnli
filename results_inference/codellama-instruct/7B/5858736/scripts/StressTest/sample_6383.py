# Define variables for the numerical entities in the premise and hypothesis
x_premise = 10
x_hypothesis = 15
hours_worked_premise = 40
hours_worked_hypothesis = 50

# Extract all quantities as valid numbers
x_premise = float(x_premise)
x_hypothesis = float(x_hypothesis)
hours_worked_premise = float(hours_worked_premise)
hours_worked_hypothesis = float(hours_worked_hypothesis)

# Check if the hypothesis value contradicts the premise
if x_hypothesis!= x_premise:
    label = "contradiction"
elif hours_worked_hypothesis!= hours_worked_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
