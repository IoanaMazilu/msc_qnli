# Define variables with representative names for the numerical entities in both inputs
hours_worked_dan = 3
hours_worked_annie = 4

# Extract all quantities as valid numbers (integers or floats)
hours_worked_dan = int(hours_worked_dan)
hours_worked_annie = int(hours_worked_annie)

# Use brief comments to explain what comparison you do between the defined variables
if hours_worked_annie <= hours_worked_dan:
    # Check if the estimate of 'hours_worked_annie' contradicts the number of hours worked by Dan
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
