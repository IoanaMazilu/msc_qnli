# Define variables for the numerical entities in the premise and hypothesis
x_premise = 0
x_hypothesis = 0
hours_worked_premise = 0
hours_worked_hypothesis = 0

# Extract all quantities as valid numbers
x_premise = float(input("Enter the value of x in the premise: "))
hours_worked_premise = float(input("Enter the number of hours worked in the premise: "))
x_hypothesis = float(input("Enter the value of x in the hypothesis: "))
hours_worked_hypothesis = float(input("Enter the number of hours worked in the hypothesis: "))

# Check if the hypothesis values and estimates do not contradict the premise ones
if x_hypothesis!= x_premise:
    label = "contradiction"
elif hours_worked_hypothesis!= hours_worked_premise:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
