# Define variables with representative names for the numerical entities in both inputs
percentage_students_with_cars_premise = 18
percentage_students_with_cars_hypothesis = 58

# Extract all quantities as valid numbers (integers or floats)
number_students_in_three_lower_grades_premise = 0
number_students_in_three_lower_grades_hypothesis = 0

# Use brief comments to explain what comparison you do between the defined variables
if percentage_students_with_cars_hypothesis <= percentage_students_with_cars_premise:
    # Check if the hypothesis value contradicts the estimate of 'percentage_students_with_cars_premise'
    label = "contradiction"
else:
    # The hypothesis value is greater than the premise estimate, so we can infer entailment
    label = "entailment"

print(label)
