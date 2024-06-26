# Define variables with representative names for the numerical entities in both inputs
num_students_morse = 1000
num_students_lower_grades = 300
percentage_students_with_cars_morse = 0.4
percentage_students_with_cars_hypothesis = 0.2

# Extract all quantities as valid numbers (integers or floats)
num_students_with_cars_morse = int(num_students_morse * percentage_students_with_cars_morse)
num_students_with_cars_hypothesis = int(num_students_morse * percentage_students_with_cars_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if num_students_with_cars_hypothesis <= num_students_with_cars_morse:
    # Check if the estimate of 'num_students_with_cars_hypothesis' contradicts the number of students with cars in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
