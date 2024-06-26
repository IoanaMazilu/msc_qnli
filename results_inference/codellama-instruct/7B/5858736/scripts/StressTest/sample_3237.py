# Define variables for the numerical entities in the premise and hypothesis
num_students_morse = 1000
percentage_students_morse_cars = 0.2
num_students_lower_grades = 300

# Extract all quantities as valid numbers
num_students_morse = int(num_students_morse)
percentage_students_morse_cars = float(percentage_students_morse_cars)
num_students_lower_grades = int(num_students_lower_grades)

# Perform calculations
num_students_morse_cars = int(num_students_morse * percentage_students_morse_cars)

# Use brief comments to explain what comparison you do between the defined variables
if num_students_morse_cars <= num_students_lower_grades:
    # Check if the number of students with cars in Morse contradicts the number of students in the three lower grades
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
