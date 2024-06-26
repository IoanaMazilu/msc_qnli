# Define variables with representative names for the numerical entities in both inputs
num_students_all_grades = 1000
percentage_students_with_cars = 0.25

# Extract all quantities as valid numbers (integers or floats)
num_students_lower_grades = num_students_all_grades * percentage_students_with_cars

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments
if num_students_lower_grades <= num_students_all_grades * 0.85:
    # Check if the estimate of 'num_students_lower_grades' contradicts the number of students in the three lower grades reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
