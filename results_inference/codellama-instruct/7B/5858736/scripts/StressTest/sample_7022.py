# Define variables with representative names for the numerical entities in both inputs
num_students_all_grades = 1000
num_students_lower_grades = 300
percentage_students_with_cars = 0.2
percentage_students_with_cars_hypothesis = 0.5

# Extract all quantities as valid numbers (integers or floats)
num_students_all_grades = int(num_students_all_grades)
num_students_lower_grades = int(num_students_lower_grades)
percentage_students_with_cars = float(percentage_students_with_cars)
percentage_students_with_cars_hypothesis = float(percentage_students_with_cars_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if percentage_students_with_cars_hypothesis <= percentage_students_with_cars:
    # Check if the estimate of 'percentage_students_with_cars_hypothesis' contradicts the number of students with cars mentioned in the premise
    label = "contradiction"
elif num_students_lower_grades!= (num_students_all_grades * percentage_students_with_cars):
    # Check if the number of students in the lower grades in the hypothesis contradicts the number of students with cars mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
