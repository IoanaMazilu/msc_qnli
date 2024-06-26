# Define variables for the numerical entities in both inputs
num_students_morse = 1000
percentage_students_morse_cars = 0.25

# Extract all quantities as valid numbers
num_students_lower_grades = 300
percentage_students_lower_grades_cars = 0.35

# Use brief comments to explain what comparison you do between the defined variables
if percentage_students_lower_grades_cars <= percentage_students_morse_cars:
    # Check if the estimate of 'percentage_students_lower_grades_cars' contradicts the percentage of students with cars in Morse
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
