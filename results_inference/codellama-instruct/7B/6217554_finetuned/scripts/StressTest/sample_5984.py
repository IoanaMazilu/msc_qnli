# define the percentage of students with cars in the premise and hypothesis
percentage_cars_premise = 25
percentage_cars_hypothesis = 85

# define the number of students in the three lower grades in the premise and hypothesis
students_lower_grades_premise = 100
students_lower_grades_hypothesis = 100

# compute the number of students with cars in the premise and hypothesis
students_cars_premise = round(students_lower_grades_premise * percentage_cars_premise / 100)
students_cars_hypothesis = round(students_lower_grades_hypothesis * percentage_cars_hypothesis / 100)

# check if the number of students with cars in the hypothesis contradicts the number of students with cars in the premise
if students_cars_hypothesis!= students_cars_premise:
    label = "contradiction"
# check if the number of students with cars in the hypothesis contradicts the number of students with cars in the premise
elif students_lower_grades_hypothesis!= students_lower_grades_premise:
    label = "contradiction"
# if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
else:
    label = "entailment"

print(label)
